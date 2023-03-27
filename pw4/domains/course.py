from .eduobj import EduObj
import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class Course(EduObj):
    def __init__(self, name: str, id: str, credits: int, marks: list) -> None:
        self.__name = name
        self.__id = id
        self.__credits = credits
        self.__marks = marks

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def credits(self) -> int:
        return self.__credits

    @property
    def marks(self) -> list:
        return self.__marks

    @name.setter
    def name(self, name: str) -> Self:
        self.__name = name
        return self

    @id.setter
    def id(self, id: str) -> Self:
        self.__id = id
        return self

    @credits.setter
    def credits(self, credits: int) -> Self:
        self.__credits = credits
        return self

    @marks.setter
    def marks(self, marks: list) -> Self:
        self.__marks = marks
        return self

    def display(self) -> None:
        print(f"- course name: {self.name}")
        print(f"- course id: {self.id}")
        print()
