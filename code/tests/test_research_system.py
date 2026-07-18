import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "code" / "scripts" / "research_system.py"
SPEC = importlib.util.spec_from_file_location("research_system", MODULE_PATH)
research_system = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(research_system)


class ResearchSystemTests(unittest.TestCase):
    def test_repository_configuration_is_valid_json(self):
        config = json.loads((ROOT / "config" / "research-system.json").read_text(encoding="utf-8"))
        self.assertEqual(config["version"], 2)
        ids = [item["id"] for item in config["collection"]["queries"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_parse_arxiv_atom(self):
        payload = b"""<?xml version='1.0' encoding='UTF-8'?>
        <feed xmlns='http://www.w3.org/2005/Atom' xmlns:arxiv='http://arxiv.org/schemas/atom'>
          <entry><id>https://arxiv.org/abs/2601.00001v2</id><updated>2026-01-02T00:00:00Z</updated>
          <published>2026-01-01T00:00:00Z</published><title>  A test   title </title><summary>Abstract.</summary>
          <author><name>Alice</name></author><arxiv:primary_category term='math.LO'/>
          <link rel='alternate' href='https://arxiv.org/abs/2601.00001'/><link title='pdf' href='https://arxiv.org/pdf/2601.00001'/>
          </entry></feed>"""
        records = research_system.parse_arxiv_atom(payload, "q", "paper")
        self.assertEqual(records[0]["source_id"], "arxiv:2601.00001")
        self.assertEqual(records[0]["title"], "A test title")
        self.assertEqual(records[0]["category"], "math.LO")

    def test_parse_openalex_json(self):
        payload = json.dumps({"results": [{
            "id": "https://openalex.org/W123",
            "display_name": "Work",
            "publication_date": "2026-01-01",
            "authorships": [{"author": {"display_name": "Bob"}}],
            "primary_location": {"landing_page_url": "https://example.test/work"},
            "best_oa_location": {"pdf_url": "https://example.test/work.pdf"},
            "open_access": {"is_oa": True},
            "type": "article",
            "doi": "https://doi.org/10.1/test"
        }]}).encode()
        records = research_system.parse_openalex_json(payload, "q", "survey")
        self.assertEqual(records[0]["source_id"], "openalex:W123")
        self.assertEqual(records[0]["doi"], "10.1/test")
        self.assertTrue(records[0]["is_oa"])

    def test_merge_records_keeps_query_provenance(self):
        base = {"source_id": "arxiv:1", "query_ids": ["a"], "doi": "", "pdf_url": ""}
        other = {"source_id": "arxiv:1", "query_ids": ["b"], "doi": "10/x", "pdf_url": "p"}
        merged = research_system.merge_records([base, other])
        self.assertEqual(merged[0]["query_ids"], ["a", "b"])
        self.assertEqual(merged[0]["doi"], "10/x")

    def test_merge_records_deduplicates_cross_source_doi(self):
        arxiv = {"source_id": "arxiv:1", "query_ids": ["a"], "doi": "10/x", "pdf_url": ""}
        openalex = {"source_id": "openalex:W1", "query_ids": ["b"], "doi": "10/X", "pdf_url": "p"}
        merged = research_system.merge_records([arxiv, openalex])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["source_aliases"], ["arxiv:1", "openalex:W1"])

    def test_known_ids_ignores_malformed_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.jsonl"
            path.write_text('{"source_id":"x"}\nnot-json\n', encoding="utf-8")
            self.assertEqual(research_system.load_known_ids(path), {"x"})


if __name__ == "__main__":
    unittest.main()
