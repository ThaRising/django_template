#!/usr/bin/env python
import os
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Union, ClassVar

PROJECT_DIRECTORY = Path.cwd()
DJANGO_DIR = Path(PROJECT_DIRECTORY) / "{{cookiecutter.project_name}}"
SETTINGS_FILE = DJANGO_DIR / "settings" / "production.py"
STATIC_REPOSITORY = ("github.com", "ThaRising", "django_template_static")

PathLike = Union[Path, str]


def generate_secret_key(settings_file_contents: list) -> list:
    secret_key_line_index = [
        i for i, ln in enumerate(contents) if re.match(r"SECRET_KEY", ln)
    ][0]
    settings_file_contents[
        secret_key_line_index
    ] = f"SECRET_KEY = '{secrets.token_hex()}'\n"
    return settings_file_contents


class CrossFilesystem:
    """
    Utilities for working between the temporary filesystem
    and the actual filesystem.
    """
    fs_to: ClassVar[PathLike] = DJANGO_DIR

    @staticmethod
    def normalize(path: PathLike) -> str:
        return os.path.abspath(path)

    def __init__(self, temp_fs: Path) -> None:
        self.temp_fs = temp_fs

    def make_relative(self, path: PathLike) -> str:
        normalized_path = self.normalize(path)
        normalized_base = self.normalize(self.fs_to)
        parts = normalized_path.split("/")

        # if the given path is from the normal fs
        if normalized_path in normalized_base:
            return self.normalize(
                "/".join(parts[len(normalized_base.split("/")):])
            )

        # if the given path is from the temp fs
        else:
            return self.normalize(
                "/".join(parts[len(self.temp_fs.parts):])
            )

    def move_from_temp(self, path: PathLike) -> None:
        join_path = self.make_relative(path)
        src = self.normalize(
            self.temp_fs.joinpath(join_path)
        )
        dest = self.normalize(
            self.fs_to.joinpath(join_path)
        )
        shutil.move(src, dest)

    def clear_temp(self) -> None:
        shutil.rmtree(self.temp_fs)


def download_custom_static() -> None:
    fs = CrossFilesystem(Path(tempfile.mkdtemp()))

    # Clone the git repository into a tempdir
    call = subprocess.Popen(
        ["git", "clone", "--depth=1", f"https://{'/'.join(STATIC_REPOSITORY)}"],
        stdout=subprocess.PIPE,
        cwd=fs.normalize(fs.temp_fs)
    )
    output, _error = call.communicate()
    if _error:
        sys.exit(_error)

    def check_instant_merge(path: Path) -> bool:
        proj_path = fs.fs_to / path.name
        if not proj_path.exists():
            fs.move_from_temp(proj_path)
            return True
        return False

    # Filter between files and directories and delete toplevel files
    files, dirs = [], []
    for item in Path(fs.fs_to).iterdir():
        files.append(item) if item.is_file() else dirs.append(item)
    for file in files:
        file.unlink()
    # If the directories dont exist we can instantly copy them
    dirs = [dir_ for dir_ in dirs if not check_instant_merge(dir_)]
    # In case all directories could be instantly merged the function can exit
    if len(dirs) < 1:
        return

    # Recursively process all trees that could not be merged
    def merge_into(paths: List[Path]):
        for item in paths:  # noqa shadows outer variable
            if item.is_dir():
                return merge_into(list(item.iterdir()))
            elif item.is_file():
                item.unlink()

            if not item.exists():
                fs.move_from_temp(fs.make_relative(item))

    merge_into(dirs)
    fs.clear_temp()
    return


if __name__ == '__main__':
    with open(SETTINGS_FILE, "r") as fin:
        contents = fin.readlines()

    contents = generate_secret_key(contents)

    with open(SETTINGS_FILE, "w") as fout:
        fout.writelines(contents)

    download_custom_static()

    sys.exit(0)
