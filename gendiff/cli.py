import argparse
# import pkg_resources
# my_version = pkg_resources.get_distribution('gendiff').version


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Compares two configuration\
                        files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='output formats: stylish, plane, json\
                         (default: "stylish")',
                        default='stylish', type=str)
    parser.add_argument('-V', '--version',
                        help='output the version info',
                        action='version',
                        version='%(prog)s {}'.format('0.1.0'))

    args = parser.parse_args()
    return args.first_file.lower(), args.second_file.lower(), args.format


path1, path2, format_name = parse_cli_args()
