import sys
import os
import textwrap

students = []
courses = []

def display(list: list):
    # TODO: do pretty print
    for _, item in enumerate(list):
        print("{id}. {name}".format(id = item["id"], name = item["name"]))

def display_marks():
    while True:
        display(courses)
        choice = int(input("choose the course you want to display marks for (0 to exit): "))

        if choice == 0:
            break

        print("displaying marks for course {course}:"
              .format(course = courses[choice-1]["name"]))

        for _, mark in enumerate(courses[choice-1]["marks"]):
            print(textwrap.dedent("""\
                {id}. {name}:
                    - midterm: {midterm}
                    - final: {final}
                """).format(id = mark["student_id"], name = mark["student_name"],
                            midterm = mark["midterm"], final = mark["final"]))

def input_students(students: list):
    students_count = int(input("give number of students to add pls: "))
    for _ in range(0, students_count):
        student = {
            "id": 0,
            "name": "",
            "dob": "",
        }

        student["id"] = len(students) + 1
        student["name"] = input("give name of student pls: ")
        student["dob"] = input("give dob of student pls (yyyy-mm-dd): ")

        students.append(student)

def input_courses(courses: list):
    courses_count = int(input("give number of courses pls: "))
    for _ in range(0, courses_count):
        course = {
            "id": 0,
            "name": "",
            "marks": [],
        }

        course["id"] = len(courses) + 1
        course["name"] = input("give name of course pls: ")

        courses.append(course)

def input_marks():
    while True:
        display(courses)
        course_choice = int(input("choose the course you want to input marks for (0 to exit): "))

        if course_choice == 0:
            break

        print("currently modifying marks for course {course}"
              .format(course = courses[course_choice-1]["name"]))

        while True:
            display(students)
            student_choice = int(input("choose the student you want to edit marks for (0 to exit): "))

            if student_choice == 0:
                break

            print("currently modifying marks for student {student} in course {course}"
                  .format(student = students[student_choice-1]["name"],
                          course = courses[course_choice-1]["name"]))

            mark = {
                "student_id": students[student_choice-1]["id"],
                "student_name": students[student_choice-1]["name"],
                "midterm": 0,
                "final": 0,
            }

            mark["midterm"] = float(input("give midterm mark pls: "))
            mark["final"] = float(input("give final mark pls: "))

            courses[course_choice-1]["marks"].append(mark)

def main():
    while True:
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

        print("proudly managing {students} students and {courses} courses"
              .format(students = len(students), courses = len(courses)))

        choice = int(input("choice: "))
        print()

        match choice:
            case 1:
                input_students(students)
            case 2:
                input_courses(courses)
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
                    display(students)
            case 5:
                if not courses:
                    print("there are no courses!")
                else:
                    display(courses)
            case 6:
                if not students:
                    print("there are no students!")
                elif not courses:
                    print("there are no courses!")
                else:
                    display_marks()
            case 7:
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
