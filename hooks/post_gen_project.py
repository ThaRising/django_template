#!/usr/bin/env python
from pathlib import Path
import secrets
import sys
import re

PROJECT_DIRECTORY = Path.cwd()
DJANGO_DIR = Path(PROJECT_DIRECTORY) / "{{cookiecutter.project_name}}"
SETTINGS_FILE = DJANGO_DIR / "settings" / "production.py"
KEYS_FILE = DJANGO_DIR / "settings" / "keys.py"
IGNORE_FILE = DJANGO_DIR.parent.parent / ".gitignore"

if __name__ == '__main__':
    # Generate Secret Key
    with open(KEYS_FILE, "r") as fin:
        contents = fin.readlines()

    secret_key_line_index = [
        i for i, ln in enumerate(contents) if re.match(r"SECRET_KEY", ln)
    ][0]
    contents[secret_key_line_index] = f"SECRET_KEY = '{secrets.token_hex()}'\n"

    with open(KEYS_FILE, "w") as fout:
        fout.writelines(contents)

    # Exclude keys file from git
    with open(IGNORE_FILE, "r") as fin:
        contents = fin.readlines()

    contents.append(f"{KEYS_FILE!s}\n")

    with open(IGNORE_FILE, "w") as fout:
        fout.writelines(contents)

    sys.exit(0)
