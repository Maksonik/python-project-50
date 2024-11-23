import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.description = "Compares two configuration files and shows a difference."
    args = parser.parse_args()

    with open(args.first_file) as file:
        data_1 = json.load(file)

    with open(args.second_file) as file:
        data_2 = json.load(file)

    print(data_1, data_2)



