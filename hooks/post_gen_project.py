#!/usr/bin/env python
from pathlib import Path
import secrets
import sys
import re
import os

PROJECT_DIRECTORY = Path.cwd()
DJANGO_DIR = Path(PROJECT_DIRECTORY) / "{{cookiecutter.project_name}}"
TEST_DIR = Path(PROJECT_DIRECTORY) / "tests"
SETTINGS_FILE = DJANGO_DIR / "settings" / "production.py"
KEYS_FILE = DJANGO_DIR / "settings" / "keys.py"
IGNORE_FILE = DJANGO_DIR.parent / ".gitignore"

CORS_INTEGRATION = {{cookiecutter.cors_integration|int}}

if __name__ == '__main__':
    # Delete CORS related files if the option is not selected
    if not CORS_INTEGRATION:
        os.remove((TEST_DIR / "inbuilts" / "test_cors.py"))

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

    contents.append(f"\n{DJANGO_DIR.name}/settings/{KEYS_FILE.name}\n")

    with open(IGNORE_FILE, "w") as fout:
        fout.writelines(contents)

    # Create keys directory for service account keys, etc.
    KEYS_FOLDER = PROJECT_DIRECTORY / "keys"
    KEYS_FOLDER.mkdir()
    (KEYS_FOLDER / ".gitkeep").touch()

    sys.exit(0)
