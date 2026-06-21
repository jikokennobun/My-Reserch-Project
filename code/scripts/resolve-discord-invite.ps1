param(
    [Parameter(Mandatory = $true)]
    [string]$InviteUrl
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ($InviteUrl -match "discord\.gg/([^/?#\s]+)") {
    $code = $Matches[1]
} elseif ($InviteUrl -match "discord\.com/invite/([^/?#\s]+)") {
    $code = $Matches[1]
} else {
    $code = $InviteUrl.Trim()
}

if ([string]::IsNullOrWhiteSpace($code)) {
    throw "Could not parse invite code."
}

$uri = "https://discord.com/api/v10/invites/$code`?with_counts=true&with_expiration=true"
$invite = Invoke-RestMethod -Method Get -Uri $uri

[pscustomobject]@{
    InviteCode = $code
    GuildId = $invite.guild.id
    GuildName = $invite.guild.name
    ChannelId = $invite.channel.id
    ChannelName = $invite.channel.name
    ApproximateMemberCount = $invite.approximate_member_count
    ApproximatePresenceCount = $invite.approximate_presence_count
    ExpiresAt = $invite.expires_at
} | Format-List

