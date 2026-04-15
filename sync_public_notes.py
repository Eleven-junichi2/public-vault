import argparse
from pathlib import Path
import shutil
import sys

# How to use:
# `uv sync` then `uv run sync_public_notes.py`

HELP = """\
Sync notes with `publish: true` from your Obsidian Vault into `content/`.

How to use:
`uv sync` then `uv run sync_public_notes.py`
"""

REPO_ROOT = Path(__file__).resolve().parent
CONTENT_DIR = REPO_ROOT / "content"


def get_vault_path() -> Path:
    return Path.home() / "Documents" / "Obsidian" / "Vault"


VAULT_PATH = get_vault_path()


def parse_publish_value(raw_value: str) -> bool:
    value = raw_value.strip().strip("'\"").lower()
    return value == "true"


def read_publish_flag(path: Path) -> bool | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        print(f"Skipping {path}: failed to read file ({exc})", file=sys.stderr)
        return None

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return False

    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            return False
        if line.startswith((" ", "\t")):
            continue
        if not line.startswith("publish:"):
            continue
        _, raw_value = line.split(":", 1)
        return parse_publish_value(raw_value)

    return False


def sync_note(path: Path) -> None:
    relative_path = path.relative_to(VAULT_PATH)
    destination = CONTENT_DIR / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, destination)
    print(f"Copied {relative_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    return parser.parse_args()


def main() -> int:
    parse_args()

    if not VAULT_PATH.exists():
        print(f"Vault not found: {VAULT_PATH}", file=sys.stderr)
        return 1

    synced = 0
    skipped = 0

    for path in VAULT_PATH.rglob("*.md"):
        publish = read_publish_flag(path)
        if publish is None:
            skipped += 1
            continue
        if not publish:
            continue
        sync_note(path)
        synced += 1

    print(f"Synced {synced} notes")
    if skipped:
        print(f"Skipped {skipped} unreadable notes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
