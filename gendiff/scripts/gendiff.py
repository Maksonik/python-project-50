import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.description = "Compares two configuration \
                        files and shows a difference."
    args = parser.parse_args()
    format = args.format or "stylish"

    result = generate_diff(args.first_file, args.second_file, format)
    print(result)
    return result
