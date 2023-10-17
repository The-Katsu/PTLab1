# -*- coding: utf-8 -*-
import argparse
import sys
from ratings.src.CalcRating import CalcRating
from ratings.src.TextDataReader import TextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()
