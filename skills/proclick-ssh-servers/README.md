# proclick-ssh-servers

Connect to Proclick's servers (`services-proclick`, `agents-proclick`)
and the `birtha` home server over SSH via the `ssh-mcp` toolset.

Read [`SKILL.md`](./SKILL.md) for the full playbook: server inventory,
naming convention, toolset, standard workflow, credentials handling,
and troubleshooting.

## Requirements

- OpenWork (or any MCP-capable agent) with the `ssh-mcp` server
  installed — see the global `~/.config/opencode/opencode.json`
  (`ssh-mcp` entry) and `~/.config/ssh-mcp/config.toml`.
- Access to the headscale tailnet (Tailscale with MagicDNS enabled on
  the client machine).
- SSH key `~/.ssh/id_ed25519` for `birtha` and `services-proclick`;
  password for `agents-proclick` via env
  `SSH_MCP_AGENTS_PROCLICK_PASSWORD` (never commit the value).

## Invoke

```text
Use $proclick-ssh-servers to check the servers / run a command / transfer files.
```
