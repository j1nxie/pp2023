import sys
import os
import textwrap

def display(l: list):
    # TODO: do pretty print
    for _, item in enumerate(l):
        print(item)

def input_students(students: list):
    students_count = int(input("give number of students pls: "))
    for i in range(0, students_count):
        student = {
            "id": 0,
            "name": "",
            "dob": "",
        }

        student["id"] = i + 1
        student["name"] = input("give name of student pls: ")
        student["dob"] = input("give dob of student pls (yyyy-mm-dd): ")

        students.append(student)

def input_courses(courses: list):
    courses_count = int(input("give number of courses pls: "))
    for i in range(0, courses_count):
        course = {
            "id": 0,
            "name": "",
            "marks": [],
        }

        course["id"] = i + 1
        course["name"] = input("give name of course pls: ")

        courses.append(course)

def main():
    students = []
    courses = []

    while True:
        print(textwrap.dedent("""\
        welcome to the student management system.
        what do you want to do?
            1 - input students info
            2 - input courses info
            3 - display students info
            4 - display courses info
            5 - exit
        """))

        print("proudly managing {students} students and {courses} courses"
              .format(students = len(students), courses = len(courses)))

        choice = int(input("choice: "))

        match choice:
            case 1:
                input_students(students)
            case 2:
                input_courses(courses)
            case 3:
                display(students)
            case 4:
                display(courses)
            case 5:
                break
            case _:
                print("invalid choice!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("system is interrupted by keyboard")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
