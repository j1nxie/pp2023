import sys
import os
import textwrap

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

students = []
courses = []

class Student:
    def __init__(self, name: str, id: str, dob: str) -> None:
        self.__name = name
        self.__id = id
        self.__dob = dob

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_dob(self) -> str:
        return self.__dob

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: str) -> Self:
        self.__id = id
        return self

    def set_dob(self, dob: str) -> Self:
        self.__dob = dob
        return self

    def display(self) -> None:
        print(f"student name: {self.__name}")
        print(f"student id: {self.__id}")
        print(f"student dob (yyyy-mm-dd): {self.__dob}")
        print()

class Course:
    def __init__(self, name: str, id: str, marks: list) -> None:
        self.__name = name
        self.__id = id
        self.__marks = marks

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_marks(self) -> list:
        return self.__marks

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: str) -> Self:
        self.__id = id
        return self

    def set_marks(self, marks: list) -> Self:
        self.__marks = marks
        return self

    def display(self) -> None:
        print(f"course name: {self.__name}")
        print(f"course id: {self.__id}")
        print()

class Mark:
    def __init__(self, student: Student, course: Course, midterm: float, final: float) -> None:
        self.__student = student
        self.__course = course
        self.__midterm = midterm
        self.__final = final

    def get_student(self) -> Student:
        return self.__student

    def get_course(self) -> Course:
        return self.__course

    def get_midterm(self) -> float:
        return self.__midterm

    def get_final(self) -> float:
        return self.__final

    def set_student(self, student: Student) -> Self:
        self.__student = student
        return self

    def set_course(self, course: Course) -> Self:
        self.__course = course
        return self

    def set_midterm(self, midterm: float) -> Self:
        self.__midterm = midterm 
        return self

    def set_final(self, final: float) -> Self:
        self.__final = final
        return self

    def display(self) -> None:
        print(f"student name: {self.__student.get_name()}")
        print(f"course: {self.__course.get_name()}")
        print(f"midterm: {self.__midterm}")
        print(f"final: {self.__final}")
        print()

def input_students():
    name = input("input student name: ")
    id = input("input student id: ")
    dob = input("input student dob: ")
    student = Student(name, id, dob)
    students.append(student)

def input_courses():
    name = input("input course name: ")
    id = input("input course id: ")
    course = Course(name, id, [])
    courses.append(course)

def display_students():
    for student in students:
        student.display()

def display_courses():
    for course in courses:
        course.display()

def display_marks():
    for (i, course) in enumerate(courses, 1):
        print(f"{i}. {course.get_name()}")

    choice = int(input("select a course: "))
    course_marks = courses[choice - 1].get_marks()
    for mark in course_marks:
        mark.display()
        print()

def main():
    print(textwrap.dedent("""\
    welcome to the student management system.
    what do you want to do?
        1 - input students info
        2 - input courses info
        3 - input marks
        4 - display students info
        5 - display courses info
        6 - display marks
        7 - exit
    """))

    while True:
        print(f"proudly managing {len(students)} students and {len(courses)} courses!")

        choice = int(input("choice: "))
        print()

        match choice:
            case 1:
                input_students()
            case 2:
                input_courses()
            case 4:
                if not students:
                    print("there are no students!")
                else:
                    display_students()
            case 5:
                if not courses:
                    print("there are no courses!")
                else:
                    display_courses()
            case 7: 
                break
            case _:
                print("unimplemented!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("system is interrupted by keyboard")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
