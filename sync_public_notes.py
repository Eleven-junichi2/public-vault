from pathlib import Path
import platform
import shutil

import frontmatter

# -- configure VAULT_PATH --
os_name = platform.system()
if os_name == "Windows":
    VAULT_PATH = Path().home() / "Documents" / "Obsidian" / "Vault"
elif os_name == "Darwin":  # macOS
    VAULT_PATH = Path().home() / "Documents" / "Obsidian" / "Vault"
else:
    VAULT_PATH = Path().home() / "Documents" / "Obsidian" / "Vault"
# ----

for path in VAULT_PATH.rglob("*.md"):
    post = frontmatter.load(str(path))
    if post.get("public", True):
        # Copy the note with overwrite if it already exists
        shutil.copy(path, Path(__file__).resolve().parent / "content" / path.name)
