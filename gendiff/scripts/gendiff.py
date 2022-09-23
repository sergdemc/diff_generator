#!/usr/bin/env python

"""
This Cli-program return different two files
 which have extension .json or .yaml.
"""

from gendiff.gen_diff import generate_diff
from gendiff.cli import path1, path2, format_name


def main():
    print(generate_diff(path1, path2, format_name))


if __name__ == '__main__':
    main()
