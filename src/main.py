import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from StudentCalculator import StudentCalculator
from YAMLDataReader import YAMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def get_current_reader(path: str) -> DataReader:
    _, file_extension = os.path.\
        splitext(path)
    match file_extension:
        case ".txt":
            return TextDataReader()
        case ".yaml":
            return YAMLDataReader()
        case _:
            raise ValueError("Неподдерживаемый формат")


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_current_reader(path)
    students = reader.read(path)
    print("Students: ", students)
    excellent_students = StudentCalculator().\
        count_excellent_students(students)
    print("Excellent students : ", excellent_students)


if __name__ == "__main__":
    main()
