#!/usr/bin/env bash
# Render a published proClick email signature as plain text.
#
# The signature is maintained as HTML with the website, so we never copy its
# values here -- we fetch the published file and render it every time.
#
# Usage:
#   get-signature.sh            # attila (default)
#   get-signature.sh hunor
#
# Source order: live site -> local checkout. Prints the plain-text block.

set -euo pipefail

NAME="${1:-attila}"
# Note: /signatures/<name>.html 308-redirects to the extensionless canonical URL.
LIVE="https://www.proclick.eu/signatures/${NAME}"
LOCAL="${HOME}/Development/proclick.ro/public/signatures/${NAME}.html"

# -L is required (the site redirects). A 3xx exits 0 with an empty body, so we
# must also treat an empty body as a failure rather than trusting the exit code.
HTML="$(curl -fsSL --max-time 15 "$LIVE" 2>/dev/null || true)"

if [ -n "${HTML//[[:space:]]/}" ]; then
  :
elif [ -f "$LOCAL" ]; then
  echo "WARN: live fetch of $LIVE empty/failed; using local checkout $LOCAL" >&2
  HTML="$(cat "$LOCAL")"
else
  echo "ERROR: cannot fetch $LIVE and no local copy at $LOCAL" >&2
  exit 1
fi

printf '%s' "$HTML" | python3 -c '
import sys, re, html

raw = sys.stdin.read()
paras = re.findall(r"<p[^>]*>(.*?)</p>", raw, flags=re.S | re.I)
SOCIAL = ("facebook.com", "instagram.com", "twitter.com", "linkedin.com")

def render(frag):
    """Text of a <p>, with anchors reduced to their visible text."""
    frag = re.sub(r"<a[^>]*>(.*?)</a>", r"\1", frag, flags=re.S | re.I)
    frag = re.sub(r"<img[^>]*>", "", frag, flags=re.I)
    frag = re.sub(r"<[^>]+>", "", frag)
    return re.sub(r"\s+", " ", html.unescape(frag)).strip()

lines, socials = [], []
for p in paras:
    for href in re.findall(r"href=\"([^\"]+)\"", p, flags=re.I):
        if any(h in href.lower() for h in SOCIAL) and href not in socials:
            socials.append(href)
    text = render(p)
    if not text:
        continue
    # the social row is images only -> drop it, we re-emit the URLs below
    if any(h in p.lower() for h in SOCIAL) and text.lower().startswith("follow us on"):
        continue
    lines.append(text)

out = "\n".join(lines)
if socials:
    out += "\nFollow us on: " + " | ".join(socials)
print(out)
'
