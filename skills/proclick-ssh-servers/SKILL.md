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
| `proclick` | `services-proclick.headscale` | services | Main company VPS — headscale, traefik, odoo, n8n, agents infra |
| `agents-proclick` | `agents-proclick.headscale` | agents-proclick | Company agents VPS — hermes, openclaw |
| `birtha` | `birtha.headscale` | n8n | Home personal server — n8n, ollama/open-webui, vexa, firecrawl |

Tailnet IPs (stable): services `100.64.0.1`, agents `100.64.0.6`,
birtha `100.64.0.4`. `headplane-proclick` (`100.64.0.2`) is the headscale
admin UI container running ON the services box, not a separate server.

## Naming convention

- Company: `<role>-proclick` (e.g. `services-proclick`, `agents-proclick`,
  `headplane-proclick`)
- Personal/home: `birtha` (owner's family name) — keep as-is
- Tailnet DNS always ends in `.headscale`

---

## Architecture

### The tailnet (who connects to whom)

- **Headscale (control server)** runs as a Docker container on
  `services-proclick`. It is the "coordination" server every other node
  talks to when joining and when doing NAT traversal; it does **not**
  carry traffic between nodes.
  - Container `headscale` (image `headscale/headscale:0.29.3`), config at
    `/root/docker/headscale/config.yaml` on the host, data in the
    `headscale_data` volume (sqlite DB + noise keys).
  - Public control URL: `https://headscale.proclick.ai` (traefik →
    container port 8080). ACL policy: `/etc/headscale/acl.json` (mounted).
  - MagicDNS on, base domain `headscale` → every node gets
    `<hostname>.headscale`. Global DNS servers: 1.1.1.1 / 8.8.8.8.
  - DERP relays: Tailscale's default DERP map (used when direct
    connections fail, e.g. some NATs).
- **Every server + device** runs `tailscaled` and joins the tailnet by
  pointing at `headscale.proclick.ai`. Members: services, agents,
  birtha, headplane-proclick (container), macbook, ipad.
- **SSH from the Mac** goes over the tailnet using MagicDNS names —
  that is what the ssh-mcp profiles use (`*.headscale`).

### `services-proclick` (100.64.0.1, public 72.60.179.200)

Main company VPS. Runs Docker with one compose project
(`/root/docker/docker-compose.yml`) plus headscale/headplane compose:

| Container | Purpose | Notes |
| --- | --- | --- |
| `headscale` | Tailscale control server | port 8080, metrics 9090 |
| `headplane` | Headscale admin UI | routed at `headscale.proclick.ai/admin` |
| `tailscale-headplane` | Tailscale identity for headplane | own node `100.64.0.2`, userspace net |
| `traefik` | Reverse proxy / TLS | 80+443, Let's Encrypt |
| `n8n` + `n8n-postgres-db` | Automation workflows | `n8n.proclick.io` |
| `odoo` + `odoo-postgres-db` | ERP (Odoo 19) | `odoo.proclick.io` / `portal.proclick.eu` |
| `gotenberg` | PDF rendering | internal |
| `browser` | Browserless/Chrome | 127.0.0.1:3000 |
| `openclaw` | OpenClaw agent (gsuite) | `openclaw.proclick.ai` |
| `opencode` | OpenCode server | 127.0.0.1:4096 |
| `a2t-dashboard-app` | Internal dashboard | :3000 internal |
| `backup` | Docker backup automation | volume snapshots |

Host services: docker, containerd, tailscaled, fail2ban.

### `agents-proclick` (100.64.0.6, public 187.124.21.99)

Company agents VPS (Hostinger). Runs agents infrastructure:

| Container | Purpose | Notes |
| --- | --- | --- |
| `hermes` | Hermes agent (gsuite) | |
| `openclaw` | OpenClaw agent (gsuite) | healthy |
| `openclaw-gdbp-openclaw-1` | Hostinger HVPS OpenClaw | exposed `0.0.0.0:48990` |
| `traefik-traefik-1` | Reverse proxy | |

Host services: docker, containerd, tailscaled. Fail2ban-style rate
limiting on SSH (see Host-specific notes).

### `birtha` (100.64.0.4) — home personal server

Runs a larger Docker stack (hostname `n8n`). Key containers:

| Container group | Purpose |
| --- | --- |
| `ollama-openwebui-*` | Open WebUI + Ollama (LLM) stack |
| `n8n` | n8n automation (n8nio/n8n) |
| `odoo19` + `odoo19-db` | Odoo 19 ERP (localhost only) |
| `vexa-v012-*` | Vexa AI stack (agent-api, meeting-api, runtime, mcp, gateway, admin-api, postgres, redis, minio) |
| `hermes-birtha-*` | Hermes agent + gateway |
| `firecrawl-*` | Firecrawl scraping + playwright + rabbitmq |
| `evolution-api` | WhatsApp/Evolution API |
| `traefik` | Reverse proxy 80/443 |

Host services: docker, containerd, tailscaled, fail2ban.

### Public exposure summary

| Domain | Server | Service |
| --- | --- | --- |
| `headscale.proclick.ai` | services | headscale (+ `/admin` = headplane) |
| `n8n.proclick.io` | services | n8n |
| `odoo.proclick.io`, `portal.proclick.eu` | services | odoo |
| `openclaw.proclick.ai` | services | openclaw |
| `traefik.proclick.io` | services | traefik dashboard |
| proclick.hu | Cloudflare (188.114.96.x) | WordPress (separate, not in tailnet) |

---

## Cloudflare infrastructure

Cloudflare is the DNS/CDN layer for the Proclick domains. Managed via a
separate Cloudflare account (OAuth login), not via SSH.

### Account

- Email: `attila.birtha@proclick.ro`
- Account ID: `fafcaa36fb222caf8ff32a61d322ffd7`
- Zones (4, all active): `birtha.ro`, `proclick.eu`, `proclick.hu`,
  `proclick.ro`
- Currently deployed: 0 Workers, 0 D1 databases, 0 KV namespaces.
  R2 is not enabled (needs opt-in in the Cloudflare dashboard).

### How to connect (3 ways, in order of preference)

1. **Cloudflare MCP server (recommended)** — hosted, covers the whole
   Cloudflare API (Workers, KV, R2, D1, Pages, zones/DNS, AI, Queues):
   - URL: `https://mcp.cloudflare.com/mcp` (Code Mode, ~1k tokens,
     2500+ endpoints)
   - In OpenWork: Settings > Extensions > Add Custom App → name
     `cloudflare`, URL above, **Requires OAuth ON** → approve in browser
     (one-time). Tools appear after restart.
   - This is the ONLY MCP setup to use. Do **not** use the npm package
     `@cloudflare/mcp-server-cloudflare` — its `zones_list` tool returns
     hardcoded mock data (`example.com`/`test.com`), a bug in v0.2.0.
2. **`wrangler` CLI** — already installed globally (`wrangler@4.86.0`).
   Authenticated via OAuth (token in
   `~/Library/Preferences/.wrangler/config/default.toml`).
   Useful for `wrangler tail`, deploy, etc. from bash.
3. **Cloudflare API directly** — `curl -H "Authorization: Bearer $TOKEN"`
   against `api.cloudflare.com/client/v4`. Token is the `oauth_token`
   field in the wrangler config file (never echo it).

### Notes

- `wrangler whoami` shows the logged-in account. Re-login with
  `wrangler login` if the token expires.
- proclick.hu WordPress is behind Cloudflare (188.114.96.x) but the
  origin server is separate from the tailnet.
- OAuth scopes include: workers:write, workers_kv:write,
  workers_scripts:write, d1:write, pages:write, zone:read, ai:write,
  queues:write, email_routing:write, etc. No R2 scope (matches R2 not
  being enabled).


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
  Docker compose lives in `/root/docker/`; backups via the `backup`
  container (`/root/docker/backup-status.sh`).
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
- Node missing from `tailscale status` → check the headscale admin
  (`headscale.proclick.ai/admin` on services) or
  `docker exec headscale headscale nodes list` on services.
