import sys
import os
import textwrap
from typing import Self


class Student:
    def __init__(self, name: str, id: int, dob: str) -> Self:
        self.__name = name
        self.__id = id
        self.__dob = dob
        return self

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_dob(self) -> int:
        return self.__dob

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: int) -> Self:
        self.__id = id
        return self

    def set_dob(self, dob: str) -> Self:
        self.__dob = dob
        return self

class Course:
    def __init__(self, name: str, id: int, marks: list) -> Self:
        self.__name = name
        self.__id = id
        self.__marks = marks
        return self

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_marks(self) -> list:
        return self.__marks

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: int) -> Self:
        self.__id = id
        return self

    def set_marks(self, marks: list) -> Self:
        self.__marks = marks
        return self

def main():
    print("hello world")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("system is interrupted by keyboard")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
