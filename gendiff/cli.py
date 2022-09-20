import argparse
# import pyproject as pyproject
# import pkg_resources
# my_version = pkg_resources.get_distribution('gendiff').version

# VERSION = pyproject.__version__


def parse_cli():
    parser = argparse.ArgumentParser(description='Compares two configuration\
     files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='output formats: stylish, plane, JSON\
                         (default: "stylish")',
                        default='stylish', type=str)
    parser.add_argument('-V', '--version',
                        help='output the version number',
                        default='', type=str)

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


path1, path2, format_name = parse_cli()
