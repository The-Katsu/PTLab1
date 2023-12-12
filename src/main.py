# -*- coding: utf-8 -*-
import argparse
import sys

from src.CalcRating import CalcRating
from src.CharacteristicsCalculator import CharacteristicsCalculator
from src.TextDataReader import TextDataReader
from src.YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    ext = path.split('.')[-1]

    reader = None

    if ext == "yaml":
        reader = YamlDataReader()
    elif ext == "txt":
        reader = TextDataReader()
    else:
        print("not found")

    students = reader.read(path)
    print("Yaml Students: ", students)
    rating = CalcRating(students).calc()
    print("Yaml Rating: ", rating)
    calculator = CharacteristicsCalculator(students)
    excellent_students = calculator.count_excellent_students()
    print(f"Yaml Number of excellent students: {excellent_students}")


if __name__ == "__main__":
    main()