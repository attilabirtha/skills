# Skill Agent Instructions: proclick-ssh-servers

This skill grants SSH access to Proclick's servers via the `ssh-mcp`
toolset. The servers are production infrastructure — treat them with care.

## Before running anything

1. Read `SKILL.md` fully.
2. Run `ssh-mcp_list-connections` to confirm the profiles are loaded
   (`birtha`, `proclick`, `agents-proclick`).
3. Use `ssh-mcp_read-command` (allowlisted read-only) whenever the task
   is a read. Use `ssh-mcp_run-command` for arbitrary commands.

## Rules

- **Never echo or log the agents-proclick password.** It lives only in
  the env var `SSH_MCP_AGENTS_PROCLICK_PASSWORD` and the ssh-mcp config.
- **Destructive commands need approval** (`ask-destructive` mode): `rm`,
  reboots, service restarts, sudo. If approval cannot be elicited, they
  are refused — that is by design.
- **agents-proclick rate-limits failed logins** (fail2ban). Wait ~20s
  between retries after a `Permission denied`; never hammer it.
- **Headplane-proclick is a container** on the services box, not a
  separate server. Do not treat `100.64.0.2` as a host you can SSH into.
- Use tailnet DNS names (`.headscale`) rather than raw IPs where
  possible.

## Conventions

- Company servers: `<role>-proclick`; home server: `birtha`.
- Multi-step work: use `open-session` (interactive) to keep CWD/env.
- File transfer: `sftp-upload` / `sftp-download` with remote paths.
