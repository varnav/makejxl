#!/usr/bin/env python3
# Based on https://geoffruddock.com/bulk-makejxl-x265-with-ffmpeg/

import os
import pathlib
import sys
from subprocess import run
from typing import Iterable

import click
from termcolor import colored

__version__ = '0.1.0'
SUPPORTED_FORMATS = ['jpeg', 'jpg', 'png', 'apng', 'gif', 'exr', 'ppm', 'pfm', 'pgx']


# Ported from: https://github.com/victordomingos/optimize-images
def search_files(dirpath: str, recursive: bool) -> Iterable[str]:
    if recursive:
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                if not os.path.isfile(os.path.join(root, f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.join(root, f)
    else:
        with os.scandir(dirpath) as directory:
            for f in directory:
                if not os.path.isfile(os.path.normpath(f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.normpath(f)


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-r', '--recursive', is_flag=True, help='Recursive')
@click.option('-s', '--speed', default='kitten', help='Speed')
def main(directory, recursive=False, speed='kitten'):
    if recursive:
        print('Processing recursively starting from', directory)
        recursive = True
    else:
        print('Processing non-recursively starting from', directory)
        recursive = False

    if not os.access(directory, os.W_OK) or not os.path.exists(directory):
        print('No such directory or not writable')
        sys.exit(1)

    for filepath in search_files(str(directory), recursive=recursive):
        fp = pathlib.PurePath(filepath)
        newpath = fp.parent.joinpath(fp.stem + '.' + 'jxl')
        convert_cmd = f'cjxl -s {speed} {fp} {newpath}'
        conversion_return_code = run(convert_cmd, shell=True).returncode
        if conversion_return_code == 0:
            print(colored(newpath, 'green'), 'ready')
        else:
            print(colored(fp, 'red'), 'error')


if __name__ == '__main__':
    main()
