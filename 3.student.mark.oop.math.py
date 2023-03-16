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

    def display(self, *args, **kwargs) -> None:
        pass

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
        print(f"- student gpa: {self.gpa}")
        print()

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
        print(f"- result: {self.result}")
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

            result = round(float(input("give result pls: ")), 1)

            mark = Mark(selected_student, selected_course, result)
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
