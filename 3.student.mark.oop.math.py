import sys
import os
import textwrap

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

students = []
courses = []

class EduObj:
    def get_class_name(self) -> str:
        return self.__class__.__name__

    def input(self, *args, **kwargs):
        pass

    def display(self, *args, **kwargs):
        pass

class Student(EduObj):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__gpa = gpa

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_dob(self) -> str:
        return self.__dob

    def get_gpa(self) -> float:
        return self.__gpa

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: str) -> Self:
        self.__id = id
        return self

    def set_dob(self, dob: str) -> Self:
        self.__dob = dob
        return self

    def set_gpa(self, gpa: float) -> Self:
        self.__gpa = gpa
        return self

    def display(self) -> None:
        print(f"student name: {self.__name}")
        print(f"student id: {self.__id}")
        print(f"student dob (yyyy-mm-dd): {self.__dob}")
        print(f"student gpa: {self.__gpa}")
        print()

class Course(EduObj):
    def __init__(self, name: str, id: str, credits: int, marks: list) -> None:
        self.__name = name
        self.__id = id
        self.__credits = credits
        self.__marks = marks

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_credits(self) -> int:
        return self.__credits

    def get_marks(self) -> list:
        return self.__marks

    def set_name(self, name: str) -> Self:
        self.__name = name
        return self

    def set_id(self, id: str) -> Self:
        self.__id = id
        return self

    def set_credits(self, credits: int) -> Self:
        self.__credits = credits
        return self

    def set_marks(self, marks: list) -> Self:
        self.__marks = marks
        return self

    def display(self) -> None:
        print(f"course name: {self.__name}")
        print(f"course id: {self.__id}")
        print()

    def __init__(self, student: Student, course: Course, midterm: float, final: float) -> None:
class Mark(EduObj):
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
    student = Student(name, id, dob, None)
    students.append(student)

def input_courses():
    name = input("input course name: ")
    id = input("input course id: ")
    credits = int(input("input course credits: "))
    course = Course(name, id, credits, [])
    courses.append(course)

def input_marks():
    for (i, course) in enumerate(courses, 1):
        print(f"{i}. {course.get_name()}")

    while True:
        course_choice = int(input("select a course (0 - exit): "))

        if course_choice == 0:
            break

        selected_course = courses[course_choice - 1]
        print(f"currently modifying marks for course {selected_course.get_name()}")

        while True:
            for (i, student) in enumerate(students, 1):
                print(f"{i}. {student.get_name()} - {student.get_id()}")

            student_choice = int(input("select a student (0 - exit): "))
            if student_choice == 0:
                break

            selected_student = students[student_choice - 1]
            print(f"currently modifying marks for student {selected_student.get_name()}")

            midterm = round(float(input("give midterm mark pls: ")), 1)
            final = round(float(input("give final mark pls: ")), 1)

            mark = Mark(selected_student, selected_course, midterm, final)
            current_mark_list = selected_course.get_marks()
            current_mark_list.append(mark)
            selected_course.set_marks(current_mark_list)

def display_objects(object_list: list):
    for (i, obj) in enumerate(object_list, 1):
        print(f"{obj.get_class_name()} {i}:")
        if isinstance(obj, EduObj):
            obj.display()

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
            case 3:
                if not students:
                    print("there are no students!")
                elif not courses:
                    print("there are no courses!")
                else:
                    input_marks()
            case 4:
                if not students:
                    print("there are no students!")
                else:
                    display_objects(students)
            case 5:
                if not courses:
                    print("there are no courses!")
                else:
                    display_objects(courses)
            case 6:
                if not students:
                    print("there are no students!")
                elif not courses:
                    print("there are no courses!")
                else:
                    display_objects(courses)
                    choice = int(input("select a course: "))
                    course_marks = courses[choice - 1].get_marks()
                    display_objects(course_marks)
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
