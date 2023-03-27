import sys
from threading import Lock
from .course import Course
from .student import Student
from .mark import Mark

if sys.version_info >= (3, 11):
    from typing import Self, Any
else:
    from typing_extensions import Self, Any

class Major():
    def __init__(self, students: list[Student], courses: list[Course]) -> None:
        self.__students = students
        self.__courses = courses

    @property
    def students(self) -> list[Student]:
        return self.__students

    @property
    def courses(self) -> list[Course]:
        return self.__courses

    @students.setter
    def students(self, students: list[Student]) -> Self:
        self.__students = students
        return self

    @courses.setter
    def courses(self, courses: list[Course]) -> Self:
        self.__courses = courses 
        return self

    def add_student(self) -> None:
        name = input("input student name: ")
        id = input("input student id: ")
        dob = input("input student dob: ")
        student = Student(name, id, dob, None)
        self.__students.append(student)

    def add_course(self) -> None:
        name = input("input course name: ")
        id = input("input course id: ")
        credits = int(input("input course credits: "))
        course = Course(name, id, credits, [])
        self.__courses.append(course)

    def add_mark(self) -> None:
        for (i, course) in enumerate(self.__courses, 1):
            print(f"{i}. {course.name}")

        while True:
            course_choice = int(input("select a course (0 - exit): "))

            if course_choice == 0:
                break

            selected_course = self.__courses[course_choice - 1]
            print(f"currently modifying marks for course {selected_course.name}")

            while True:
                for (i, student) in enumerate(self.__students, 1):
                    print(f"{i}. {student.name} - {student.id}")

                student_choice = int(input("select a student (0 - exit): "))
                if student_choice == 0:
                    for (i, course) in enumerate(self.__courses, 1):
                        print(f"{i}. {course.name}")
                    break

                selected_student = self.__students[student_choice - 1]
                print(f"currently modifying marks for student {selected_student.name}")

                result = float(input("give result pls: "))

                mark = Mark(selected_student, selected_course, result)
                selected_course.marks.append(mark)
