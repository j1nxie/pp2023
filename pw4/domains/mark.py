from domains import EduObj, Student, Course
import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class Mark(EduObj):
    def __init__(self, student: Student, course: Course, result: float) -> None:
        self.__student = student
        self.__course = course
        self.__result = result

    @property
    def student(self) -> Student:
        return self.__student

    @property
    def course(self) -> Course:
        return self.__course

    @property
    def result(self) -> float:
        return self.__result

    @student.setter
    def student(self, student: Student) -> Self:
        self.__student = student
        return self

    @course.setter
    def course(self, course: Course) -> Self:
        self.__course = course
        return self

    @result.setter
    def result(self, result: float) -> Self:
        self.__result = result
        return self

    def display(self) -> None:
        print(f"- student name: {self.student.name}")
        print(f"- course: {self.course.name}")
        print(f"- result: {round(self.result, 1)}")
        print()


