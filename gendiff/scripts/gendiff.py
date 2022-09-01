#!/usr/bin/env python
"""This Cli-program help you to different two files which have formats .json or .yaml."""

from gendiff import cli


def main():
    return cli.parse_args()


if __name__ == '__main__':
    main()
