from domains import EduObj
import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class Student(EduObj):
    def __init__(self, name: str, id: str, dob: str, gpa: float | None) -> None:
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__gpa = gpa

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def dob(self) -> str:
        return self.__dob

    @property
    def gpa(self) -> float | None:
        return self.__gpa

    @name.setter
    def name(self, name: str) -> Self:
        self.__name = name
        return self

    @id.setter
    def id(self, id: str) -> Self:
        self.__id = id
        return self

    @dob.setter
    def dob(self, dob: str) -> Self:
        self.__dob = dob
        return self

    @gpa.setter
    def gpa(self, gpa: float | None) -> Self:
        self.__gpa = gpa
        return self

    def display(self) -> None:
        print(f"- student name: {self.name}")
        print(f"- student id: {self.id}")
        print(f"- student dob (yyyy-mm-dd): {self.dob}")
        if self.gpa:
            print(f"- student gpa: {round(self.gpa, 1)}")
        print()
