#!/usr/bin/env python
from pathlib import Path
import secrets
import sys

PROJECT_DIRECTORY = Path.cwd()
DJANGO_DIR = Path(PROJECT_DIRECTORY) / "{{cookiecutter.project_name}}"
SETTINGS_FILE = DJANGO_DIR / "settings" / "production.py"


def find_key_linenr(content: list) -> int:
    for i, line in enumerate(content):
        if line == "SECRET_KEY":
            return i


if __name__ == '__main__':
    print(SETTINGS_FILE)
    with open(SETTINGS_FILE, "r") as fin:
        contents = fin.readlines()

    check_contents = [[ln.strip() for ln in line][0] for line in contents]

    contents[find_key_linenr(check_contents)] = f"SECRET_KEY = {secrets.token_hex()}\n"
    with open(SETTINGS_FILE, "w") as fout:
        fout.writelines(contents)
    sys.exit(0)
