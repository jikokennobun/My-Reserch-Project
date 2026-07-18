#!/usr/bin/env python3
"""Small, dependency-free control plane for the semi-automated research system.

It deliberately automates intake and bookkeeping, not acceptance of research
claims. Network collection stores candidates and stable source identifiers only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Iterable
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


DEFAULT_ROOT = Path(__file__).resolve().parents[2]
JST = dt.timezone(dt.timedelta(hours=9), name="JST")
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
USER_AGENT = "My-Reserch-Project/2.0 (semi-automated literature intake)"


def now_jst() -> dt.datetime:
    return dt.datetime.now(JST)


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def safe_markdown(value: str | None) -> str:
    return clean_text(value).replace("|", "\\|")


def relative_path(root: Path, configured: str) -> Path:
    candidate = (root / configured).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"Configured path escapes repository: {configured}") from exc
    return candidate


def load_config(root: Path) -> dict[str, Any]:
    path = root / "config" / "research-system.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def fetch_bytes(url: str, timeout: int = 30, headers: dict[str, str] | None = None) -> bytes:
    request_headers = {"User-Agent": USER_AGENT, "Accept": "application/json, application/atom+xml;q=0.9, */*;q=0.1"}
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def parse_arxiv_atom(payload: bytes, query_id: str, kind: str) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    records: list[dict[str, Any]] = []
    for entry in root.findall(f"{ATOM}entry"):
        raw_id = clean_text(entry.findtext(f"{ATOM}id"))
        arxiv_id = raw_id.rstrip("/").split("/")[-1]
        base_id = re.sub(r"v\d+$", "", arxiv_id)
        authors = [clean_text(node.findtext(f"{ATOM}name")) for node in entry.findall(f"{ATOM}author")]
        alternate_url = raw_id
        pdf_url = ""
        for link in entry.findall(f"{ATOM}link"):
            rel = link.attrib.get("rel", "")
            title = link.attrib.get("title", "")
            href = link.attrib.get("href", "")
            if rel == "alternate" and href:
                alternate_url = href
            if title == "pdf" and href:
                pdf_url = href
        primary = entry.find(f"{ARXIV}primary_category")
        category = primary.attrib.get("term", "") if primary is not None else ""
        records.append(
            {
                "source_id": f"arxiv:{base_id}",
                "source": "arXiv",
                "query_ids": [query_id],
                "kind": kind,
                "title": clean_text(entry.findtext(f"{ATOM}title")),
                "authors": authors,
                "published": clean_text(entry.findtext(f"{ATOM}published")),
                "updated": clean_text(entry.findtext(f"{ATOM}updated")),
                "url": alternate_url,
                "pdf_url": pdf_url,
                "doi": clean_text(entry.findtext(f"{ARXIV}doi")),
                "category": category,
                "abstract": clean_text(entry.findtext(f"{ATOM}summary")),
            }
        )
    return records


def collect_arxiv(query: str, query_id: str, kind: str, limit: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": limit,
            "sortBy": "lastUpdatedDate",
            "sortOrder": "descending",
        }
    )
    payload = fetch_bytes(f"https://export.arxiv.org/api/query?{params}")
    return parse_arxiv_atom(payload, query_id, kind)


def parse_openalex_json(payload: bytes, query_id: str, kind: str) -> list[dict[str, Any]]:
    document = json.loads(payload.decode("utf-8"))
    records: list[dict[str, Any]] = []
    for work in document.get("results", []):
        work_id = clean_text(work.get("id"))
        source_id = f"openalex:{work_id.rstrip('/').split('/')[-1]}"
        authors = []
        for authorship in work.get("authorships") or []:
            name = clean_text((authorship.get("author") or {}).get("display_name"))
            if name:
                authors.append(name)
        primary = work.get("primary_location") or {}
        best_oa = work.get("best_oa_location") or {}
        open_access = work.get("open_access") or {}
        doi = clean_text(work.get("doi"))
        doi = re.sub(r"^https?://doi\.org/", "", doi, flags=re.IGNORECASE)
        url = clean_text(primary.get("landing_page_url")) or clean_text(best_oa.get("landing_page_url")) or work_id
        records.append(
            {
                "source_id": source_id,
                "source": "OpenAlex",
                "query_ids": [query_id],
                "kind": kind,
                "title": clean_text(work.get("display_name") or work.get("title")),
                "authors": authors,
                "published": clean_text(work.get("publication_date")),
                "updated": clean_text(work.get("updated_date")),
                "url": url,
                "pdf_url": clean_text(best_oa.get("pdf_url")),
                "doi": doi,
                "category": clean_text(work.get("type")),
                "abstract": "",
                "is_oa": bool(open_access.get("is_oa")),
            }
        )
    return records


def collect_openalex(
    query: str,
    query_id: str,
    kind: str,
    limit: int,
    lookback_days: int,
    api_key: str | None,
) -> list[dict[str, Any]]:
    start_date = (dt.date.today() - dt.timedelta(days=lookback_days)).isoformat()
    params: dict[str, Any] = {
        "search": query,
        "filter": f"from_publication_date:{start_date}",
        "sort": "publication_date:desc",
        "per_page": limit,
    }
    headers: dict[str, str] = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    contact = os.environ.get("RESEARCH_CONTACT_EMAIL", "").strip()
    if contact:
        headers["mailto"] = contact
    payload = fetch_bytes(f"https://api.openalex.org/works?{urllib.parse.urlencode(params)}", headers=headers)
    return parse_openalex_json(payload, query_id, kind)


def merge_records(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    source_index: dict[str, str] = {}
    doi_index: dict[str, str] = {}
    for record in records:
        doi = clean_text(record.get("doi")).lower()
        source_id = record["source_id"]
        key = source_index.get(source_id) or (doi_index.get(doi) if doi else None)
        if key is None:
            key = f"doi:{doi}" if doi else source_id
        if key not in merged:
            record["source_aliases"] = [source_id]
            merged[key] = record
            source_index[source_id] = key
            if doi:
                doi_index[doi] = key
            continue
        merged[key]["query_ids"] = sorted(set(merged[key].get("query_ids", [])) | set(record.get("query_ids", [])))
        merged[key]["source_aliases"] = sorted(set(merged[key].get("source_aliases", [])) | {source_id})
        source_index[source_id] = key
        if doi:
            doi_index[doi] = key
        if not merged[key].get("doi") and record.get("doi"):
            merged[key]["doi"] = record["doi"]
        if not merged[key].get("pdf_url") and record.get("pdf_url"):
            merged[key]["pdf_url"] = record["pdf_url"]
    return list(merged.values())


def load_known_ids(catalog: Path) -> set[str]:
    if not catalog.exists():
        return set()
    known: set[str] = set()
    for line in catalog.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            known.add(record["source_id"])
            known.update(record.get("source_aliases", []))
        except (json.JSONDecodeError, KeyError):
            continue
    return known


def render_intake(records: list[dict[str, Any]], generated: dt.datetime, errors: list[str]) -> str:
    lines = [
        "---",
        "type: literature-intake",
        f"date: {generated.date().isoformat()}",
        f"generated_at: {generated.isoformat(timespec='seconds')}",
        "generated_by: code/scripts/research_system.py",
        "---",
        "",
        f"# Literature Intake — {generated.date().isoformat()}",
        "",
        "自動収集された候補であり、本文確認前には引用しない。",
        "",
    ]
    for record in records:
        title = safe_markdown(record.get("title")) or "Untitled"
        url = record.get("url") or ""
        lines.extend(
            [
                f"## [{title}]({url})" if url else f"## {title}",
                "",
                f"- source_id: `{record['source_id']}`",
                f"- source: {record.get('source', '')}",
                f"- kind: {record.get('kind', '')}",
                f"- matched_queries: {', '.join(record.get('query_ids', []))}",
                f"- authors: {', '.join(record.get('authors', []))}",
                f"- published: {record.get('published', '')}",
                f"- updated: {record.get('updated', '')}",
                f"- category/type: {record.get('category', '')}",
                f"- doi: {record.get('doi', '')}",
                f"- pdf_url: {record.get('pdf_url', '')}",
                f"- open_access_metadata: {record.get('is_oa', 'unknown')}",
                "",
                "### Triage",
                "",
                "- [ ] Active Goalに直接関係する",
                "- [ ] 原文へアクセスできる",
                "- [ ] 主張レベルで本文を確認した",
                "- decision: `candidate`",
                "- relation_to_goal:",
                "- strongest_relevant_claim:",
                "- rejection_reason:",
                "",
            ]
        )
        abstract = clean_text(record.get("abstract"))
        if abstract:
            lines.extend(["### Abstract (source metadata)", "", abstract[:1200], ""])
    if errors:
        lines.extend(["## Collection warnings", ""])
        lines.extend(f"- {safe_markdown(error)}" for error in errors)
        lines.append("")
    return "\n".join(lines)


def collect_command(root: Path, config: dict[str, Any], dry_run: bool) -> int:
    collection = config["collection"]
    queries = collection.get("queries", [])
    if dry_run:
        print(f"Configured queries: {len(queries)}")
        for item in queries:
            sources = ", ".join(key for key in ("arxiv", "openalex") if item.get(key))
            print(f"- {item['id']} [{item['kind']}]: {sources}")
        return 0

    max_results = int(collection.get("max_results_per_query", 5))
    lookback_days = int(collection.get("lookback_days", 30))
    arxiv_delay = float(collection.get("arxiv_delay_seconds", 3))
    api_key = os.environ.get("OPENALEX_API_KEY", "").strip() or None
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    calls = 0
    successes = 0
    for item in queries:
        query_id = item["id"]
        kind = item["kind"]
        if item.get("arxiv"):
            if calls:
                time.sleep(arxiv_delay)
            calls += 1
            try:
                records.extend(collect_arxiv(item["arxiv"], query_id, kind, max_results))
                successes += 1
            except (urllib.error.URLError, TimeoutError, ET.ParseError) as exc:
                errors.append(f"arXiv {query_id}: {exc}")
        if item.get("openalex"):
            calls += 1
            try:
                records.extend(collect_openalex(item["openalex"], query_id, kind, max_results, lookback_days, api_key))
                successes += 1
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                errors.append(f"OpenAlex {query_id}: {exc}")

    catalog = relative_path(root, config["paths"]["literature_catalog"])
    inbox = relative_path(root, config["paths"]["literature_inbox"])
    known = load_known_ids(catalog)
    candidates = [
        record
        for record in merge_records(records)
        if not (set(record.get("source_aliases", [record["source_id"]])) & known)
    ]
    candidates.sort(key=lambda item: item.get("published", ""), reverse=True)
    generated = now_jst()

    if candidates:
        inbox.mkdir(parents=True, exist_ok=True)
        output = inbox / f"{generated.date().isoformat()}.md"
        rendered = render_intake(candidates, generated, errors)
        if output.exists():
            previous = output.read_text(encoding="utf-8").rstrip()
            rendered = previous + "\n\n---\n\n" + rendered
        output.write_text(rendered.rstrip() + "\n", encoding="utf-8")
        catalog.parent.mkdir(parents=True, exist_ok=True)
        with catalog.open("a", encoding="utf-8", newline="\n") as handle:
            for record in candidates:
                record["collected_at"] = generated.isoformat(timespec="seconds")
                handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"Added {len(candidates)} candidate(s): {output.relative_to(root)}")
    else:
        print("No new literature candidates.")

    for warning in errors:
        print(f"WARNING: {warning}", file=sys.stderr)
    return 0 if successes else 2


def required_files(config: dict[str, Any]) -> list[str]:
    role_files = [
        ".agents/leader.md",
        ".agents/ideator.md",
        ".agents/formulator.md",
        ".agents/theory-maker.md",
        ".agents/problem-solver.md",
        ".agents/skeptic.md",
        ".agents/reviewer-primary.md",
        ".agents/reviewer-secondary.md",
        ".agents/writer.md",
        ".agents/archivist.md",
    ]
    return [
        config["entrypoint"],
        "docs/research-system-v2.md",
        "docs/prompts/research-cycle.md",
        "research/templates/goal.md",
        "research/templates/problem.md",
        "research/templates/review.md",
        "research/meta/motivation.md",
        config["paths"]["active_goal"],
        *role_files,
    ]


def validation_results(root: Path, config: dict[str, Any]) -> list[tuple[bool, str]]:
    results: list[tuple[bool, str]] = []
    results.append((config.get("version") == 2, "configuration version is 2"))
    for configured in required_files(config):
        try:
            path = relative_path(root, configured)
            results.append((path.is_file(), f"required file: {configured}"))
        except ValueError:
            results.append((False, f"unsafe configured path: {configured}"))
    for key in ("problems", "literature_inbox", "cycles", "reviews", "reflections", "improvements"):
        configured = config["paths"][key]
        try:
            path = relative_path(root, configured)
            results.append((path.is_dir(), f"required directory: {configured}"))
        except ValueError:
            results.append((False, f"unsafe configured path: {configured}"))

    goal_path = relative_path(root, config["paths"]["active_goal"])
    goal_text = goal_path.read_text(encoding="utf-8") if goal_path.exists() else ""
    for heading in ("## Objective", "## In scope", "## Out of scope", "## Done criteria", "## Evidence required", "## Decision log"):
        results.append((heading in goal_text, f"active goal section: {heading}"))
    query_ids = [item.get("id") for item in config.get("collection", {}).get("queries", [])]
    results.append((len(query_ids) == len(set(query_ids)) and all(query_ids), "collection query IDs are unique"))
    return results


def validate_command(root: Path, config: dict[str, Any], quiet: bool = False) -> int:
    results = validation_results(root, config)
    if not quiet:
        for ok, label in results:
            print(f"[{'OK' if ok else 'FAIL'}] {label}")
        failures = sum(not ok for ok, _ in results)
        print(f"\nValidation: {len(results) - failures} passed, {failures} failed")
    return 0 if all(ok for ok, _ in results) else 1


def count_files(path: Path, pattern: str = "*.md") -> int:
    return len(list(path.rglob(pattern))) if path.exists() else 0


def count_cycle_packets(path: Path) -> int:
    return sum(1 for child in path.iterdir() if child.is_dir() and (child / "manifest.json").is_file()) if path.exists() else 0


def status_command(root: Path, config: dict[str, Any]) -> int:
    active_goal = relative_path(root, config["paths"]["active_goal"])
    goal_text = active_goal.read_text(encoding="utf-8") if active_goal.exists() else ""
    goal_id = re.search(r"(?m)^id:\s*(.+)$", goal_text)
    goal_status = re.search(r"(?m)^status:\s*(.+)$", goal_text)
    print("Research System v2")
    print(f"- active goal: {goal_id.group(1).strip() if goal_id else 'missing'} ({goal_status.group(1).strip() if goal_status else 'unknown'})")
    print(f"- literature intake files: {max(0, count_files(relative_path(root, config['paths']['literature_inbox'])) - 1)}")
    print(f"- problem cards: {max(0, count_files(relative_path(root, config['paths']['problems'])) - 1)}")
    print(f"- research-cycle packets: {count_cycle_packets(relative_path(root, config['paths']['cycles']))}")
    print(f"- standalone reflection files: {max(0, count_files(relative_path(root, config['paths']['reflections'])) - 1)}")
    validation = validate_command(root, config, quiet=True)
    print(f"- structure: {'valid' if validation == 0 else 'needs attention'}")
    return validation


def replace_frontmatter_value(text: str, key: str, value: str) -> str:
    pattern = rf"(?m)^{re.escape(key)}:.*$"
    return re.sub(pattern, f"{key}: {value}", text, count=1)


def render_template(path: Path, values: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in values.items():
        text = replace_frontmatter_value(text, key, value)
    return text


def latest_markdown(directory: Path, exclude_names: set[str] | None = None) -> Path | None:
    if not directory.exists():
        return None
    excluded = exclude_names or set()
    candidates = [path for path in directory.rglob("*.md") if path.name not in excluded]
    return max(candidates, key=lambda path: path.stat().st_mtime) if candidates else None


def markdown_link(from_directory: Path, target: Path, label: str) -> str:
    relative = os.path.relpath(target, from_directory).replace("\\", "/")
    return f"[{label}]({relative})"


def render_context_packet(
    root: Path,
    config: dict[str, Any],
    destination: Path,
    cycle_id: str,
    goal: str,
    focus: str,
    generated: dt.datetime,
) -> str:
    configured_sources = [
        ("Active Goal", relative_path(root, config["paths"]["active_goal"])),
        ("Research motivation", root / "research" / "meta" / "motivation.md"),
        ("Researcher model", relative_path(root, config["paths"]["researcher_model"])),
        ("Definitions", root / "research" / "definitions.md"),
        ("Open-problem index", root / "research" / "open_problems.md"),
        ("Research questions", root / "research" / "ideas" / "research-questions.md"),
        ("Bibliography", root / "research" / "bibliography.md"),
        ("Obsidian research index", root / "research" / "notes" / "obsidian-research-index.md"),
        ("Drive reference access", root / "research" / "literature" / "drive-access.md"),
    ]
    latest_intake = latest_markdown(relative_path(root, config["paths"]["literature_inbox"]), {"README.md"})
    latest_reflection = latest_markdown(relative_path(root, config["paths"]["reflections"]), {"README.md"})
    if latest_intake:
        configured_sources.append(("Latest literature intake", latest_intake))
    if latest_reflection:
        configured_sources.append(("Latest standalone reflection", latest_reflection))

    lines = [
        "---",
        "type: research-context-packet",
        f"cycle: {cycle_id}",
        f"goal: {goal}",
        f"generated_at: {generated.isoformat(timespec='seconds')}",
        "---",
        "",
        "# Research Context Packet",
        "",
        f"- Focus: {focus}",
        "- Rule: source links are context candidates; read the relevant section directly before making a claim.",
        "",
        "## Canonical context",
        "",
        "| Source | Last modified | Link |",
        "| --- | --- | --- |",
    ]
    for label, target in configured_sources:
        if not target.exists():
            lines.append(f"| {label} | missing | `{target.relative_to(root)}` |")
            continue
        modified = dt.datetime.fromtimestamp(target.stat().st_mtime, JST).isoformat(timespec="minutes")
        lines.append(f"| {label} | {modified} | {markdown_link(destination, target, label)} |")
    lines.extend(
        [
            "",
            "## Context selection log",
            "",
            "実際に読んだファイルと、今回の焦点へ与えた差分を記す。",
            "",
            "| Source | Relevant section/claim | Difference made |",
            "| --- | --- | --- |",
            "",
            "## Missing context / access gaps",
            "",
            "- ",
            "",
        ]
    )
    return "\n".join(lines)


def init_cycle_command(root: Path, config: dict[str, Any], goal: str, focus: str) -> int:
    generated = now_jst()
    cycle_id = f"CYCLE-{generated.strftime('%Y%m%d-%H%M%S')}"
    directory_name = f"{generated.strftime('%Y-%m-%d-%H%M%S')}-{re.sub(r'[^a-z0-9-]+', '-', goal.lower()).strip('-')}"
    cycles_root = relative_path(root, config["paths"]["cycles"])
    destination = cycles_root / directory_name
    if destination.exists():
        print(f"Cycle already exists: {destination}", file=sys.stderr)
        return 1
    destination.mkdir(parents=True)
    timestamp = generated.isoformat(timespec="seconds")
    date = generated.date().isoformat()
    template_root = root / "research" / "templates"

    cycle = render_template(template_root / "cycle.md", {"id": cycle_id, "status": "scoped", "goal": goal, "created": timestamp, "updated": timestamp})
    cycle = cycle.replace("- Goal:", f"- Goal: {goal}", 1)
    cycle = cycle.replace("- Focus:", f"- Focus: {focus}", 1)
    cycle = cycle.replace("- Primary:", "- Primary: [review-primary.md](review-primary.md)", 1)
    cycle = cycle.replace("- Secondary:", "- Secondary: [review-secondary.md](review-secondary.md)", 1)
    cycle = cycle.replace("## Reflection link\n", "## Reflection link\n\n[reflection.md](reflection.md)\n", 1)
    (destination / "cycle.md").write_text(cycle, encoding="utf-8")

    primary = render_template(template_root / "review.md", {"reviewer_role": "primary", "reviewed_object": cycle_id, "created": date})
    secondary = render_template(template_root / "review.md", {"reviewer_role": "secondary", "reviewed_object": cycle_id, "created": date})
    reflection = render_template(template_root / "reflection.md", {"cycle": cycle_id, "goal": goal, "created": date})
    improvement = render_template(template_root / "improvement.md", {"id": f"IMP-{generated.strftime('%Y%m%d')}-01", "created": date, "updated": date})
    chapter = render_template(template_root / "chapter.md", {"id": "CH-01", "parent_goal": goal, "created": date, "updated": date})
    (destination / "review-primary.md").write_text(primary, encoding="utf-8")
    (destination / "review-secondary.md").write_text(secondary, encoding="utf-8")
    (destination / "reflection.md").write_text(reflection, encoding="utf-8")
    (destination / "improvement.md").write_text(improvement, encoding="utf-8")
    (destination / "chapter-01.md").write_text(chapter, encoding="utf-8")
    context = render_context_packet(root, config, destination, cycle_id, goal, focus, generated)
    (destination / "context.md").write_text(context, encoding="utf-8")
    manifest = {
        "cycle_id": cycle_id,
        "goal": goal,
        "focus": focus,
        "created": timestamp,
        "required_files": ["context.md", "cycle.md", "review-primary.md", "review-secondary.md", "reflection.md", "improvement.md", "chapter-01.md"],
    }
    (destination / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Created {cycle_id}: {destination.relative_to(root)}")
    print("Next: fill Scope and Context read, then run Ideator A/B independently.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Control plane for Research System v2")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="repository root (mainly for tests)")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate required structure and contracts")
    subparsers.add_parser("status", help="show the active goal and store counts")
    collect = subparsers.add_parser("collect", help="collect literature candidates")
    collect.add_argument("--dry-run", action="store_true", help="show configured queries without network or writes")
    cycle = subparsers.add_parser("init-cycle", help="create a complete research-cycle packet")
    cycle.add_argument("--goal", required=True, help="active goal ID")
    cycle.add_argument("--focus", required=True, help="bounded focus for this cycle")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        config = load_config(root)
        if args.command == "validate":
            return validate_command(root, config)
        if args.command == "status":
            return status_command(root, config)
        if args.command == "collect":
            return collect_command(root, config, args.dry_run)
        if args.command == "init-cycle":
            return init_cycle_command(root, config, args.goal, args.focus)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
