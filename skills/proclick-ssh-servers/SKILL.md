---
name: proclick-ssh-servers
description: |
  Connect to Proclick's servers (services-proclick, agents-proclick) and
  the birtha home server over SSH via the ssh-mcp toolset. Triggers when
  the user asks to run commands, check status, read logs, transfer files,
  or work on the services box, the agents box, or the home server (n8n),
  or mentions the headscale tailnet / .headscale hostnames.
---

# SSH Access to Proclick's Servers

Connect to the Proclick servers through the SSH MCP toolset
(`ssh-mcp_*` tools). All servers are on a private Tailscale/headscale
tailnet; all SSH profiles log in as root.

## Server inventory

| MCP profile | Tailnet DNS | Hostname | Role |
| --- | --- | --- | --- |
| `proclick` | `services-proclick.headscale` | services | Company VPS — services, odoo, headscale/headplane, traefik |
| `agents-proclick` | `agents-proclick.headscale` | agents-proclick | Company VPS — agents infrastructure |
| `birtha` | `birtha.headscale` | n8n | Home personal server — runs n8n automation |

Tailnet IPs (stable): services `100.64.0.1`, agents `100.64.0.6`,
birtha `100.64.0.4`. `headplane-proclick` (`100.64.0.2`) is the headscale
admin UI container running ON the services box, not a separate server.

## Naming convention

- Company: `<role>-proclick` (e.g. `services-proclick`, `agents-proclick`,
  `headplane-proclick`)
- Personal/home: `birtha` (owner's family name) — keep as-is
- Tailnet DNS always ends in `.headscale`

## Toolset (11 tools, from ssh-mcp v2)

`list-connections` · `open-session` / `close-session` ·
`read-session-output` · `read-command` (allowlisted read-only) ·
`run-command` (arbitrary; destructive needs approval) ·
`privileged-command` (sudo; always needs approval) ·
`sftp-upload` / `sftp-download` · `signal-process` · `list-sessions`

## Standard workflow

1. **Check what's reachable first** — `ssh-mcp_list-connections`.
   Everything listed = profile configured. A `[disconnected]` state is
   normal; it connects on first command.
2. **Run a command** — `ssh-mcp_run-command` with `profile` and
   `command`, e.g. `df -h`, `systemctl status n8n`, `docker ps`.
3. **Read-only when possible** — prefer `ssh-mcp_read-command` for
   allowlisted reads (`ls`, `cat`, `grep`, `df`, `stat`). It skips the
   approval gate.
4. **Interactive session for multi-step work** — `open-session`
   (type `interactive`) keeps CWD/env between commands; run subsequent
   commands with `session` set. `type: background` + `read-session-output`
   for long-running things like `tail -f`.
5. **File transfer** — `sftp-upload` (content + remotePath) and
   `sftp-download` (remotePath).

## Auth & credentials

- birtha, proclick: SSH key `~/.ssh/id_ed25519` (also in the Mac SSH agent)
- agents-proclick: password auth. The password lives in the ssh-mcp MCP
  config as env `SSH_MCP_AGENTS_PROCLICK_PASSWORD` (global
  `~/.config/opencode/opencode.json`) and in
  `~/.config/ssh-mcp/config.toml`. Never echo the value.

## Approval mode

Config uses `ask-destructive`: read/safe commands run freely; destructive
(`rm`, reboots, service restarts, etc.) and sudo require the user's
approval prompt. On OpenWork, if approval cannot be elicited, destructive
commands are refused — that is by design, not a bug.

## Host-specific notes

- **services-proclick** — runs the headscale control server + headplane
  admin UI (container `tailscale-headplane` has its own tailnet identity
  `100.64.0.2`), plus odoo, traefik, n8n-postgres, gotenberg, browserless.
- **agents-proclick** — fail2ban-style rate limiting: several rapid
  failed logins temporarily lock out the IP (looks like
  "Permission denied" even with a correct password). Wait ~20s and retry;
  normal one-at-a-time use never hits it.
- **birtha** — n8n runs in Docker (container `n8n`, port 5678). Load can
  spike; check `uptime` / `docker stats` if it feels slow.

## Troubleshooting

- `Permission denied (publickey,password)` on agents-proclick → rate
  limit or wrong password; wait and retry, check env var is set.
- Host key prompt → TOFU; accept on first connect.
- Profile missing from `list-connections` → check
  `~/.config/ssh-mcp/config.toml` (must be `chmod 600`, dir `700`) and
  that the MCP server loaded (may need an OpenWork restart).
- DNS `Name or service not known` → the box's own MagicDNS may be
  disabled; resolve from the Mac with `dscacheutil -q host -a name <host>`
  or ping the tailnet IP directly.
