#!/usr/bin/env python
from pathlib import Path
import secrets
import sys
import re

PROJECT_DIRECTORY = Path.cwd()
DJANGO_DIR = Path(PROJECT_DIRECTORY) / "{{cookiecutter.project_name}}"
SETTINGS_FILE = DJANGO_DIR / "settings" / "production.py"

if __name__ == '__main__':
    with open(SETTINGS_FILE, "r") as fin:
        contents = fin.readlines()

    secret_key_line_index = [
        i for i, ln in enumerate(contents) if re.match(r"SECRET_KEY", ln)
    ][0]
    contents[secret_key_line_index] = f"SECRET_KEY = '{secrets.token_hex()}'\n"

    with open(SETTINGS_FILE, "w") as fout:
        fout.writelines(contents)

    sys.exit(0)
