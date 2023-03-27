from domains import EduObj, Major
import numpy
import textwrap

def display_objects(object_list: list):
    for (i, obj) in enumerate(object_list, 1):
        print(f"{obj.get_class_name()} {i}:")
        if isinstance(obj, EduObj):
            obj.display()

def calculate_gpa(major: Major) -> None:
    row = len(major.courses)
    col = len(major.students)
    matrix = numpy.zeros(shape=(row, col))
    credits_list = []

    for (i, course) in enumerate(major.courses):
        credits_list.append(course.credits)
        for mark in course.marks:
            matrix[i] = mark.result

    transposed_matrix = matrix.transpose()

    for (i, row) in enumerate(transposed_matrix):
        total = 0
        for (j, column) in enumerate(row):
            total += column * credits_list[j]
        gpa = total / sum(credits_list)
        major.students[i].gpa = gpa

def outputs(major: Major):
    print(textwrap.dedent("""\
    welcome to the student management system.
    what do you want to do?
        1 - display students info
        2 - display courses info
        3 - display marks
        4 - calculate gpa for all students
        5 - exit
    """))

    while True:
        print(f"proudly managing {len(major.students)} students and {len(major.courses)} courses!")

        choice = int(input("choice: "))
        print()

        match choice:
            case 1:
                if not major.students:
                    print("there are no students!")
                else:
                    display_objects(major.students)
            case 2:
                if not major.courses:
                    print("there are no courses!")
                else:
                    display_objects(major.courses)
            case 3:
                if not major.students:
                    print("there are no students!")
                elif not major.courses:
                    print("there are no courses!")
                else:
                    display_objects(major.courses)
                    choice = int(input("select a course: "))
                    course_marks = major.courses[choice - 1].marks
                    if not course_marks:
                        print("course has no marks!")
                    else:
                        display_objects(course_marks)
            case 4:
                if not major.students:
                    print("there are no students!")
                elif not major.courses:
                    print("there are no courses!")
                else:
                    calculate_gpa(major)
            case 5:
                print("see you next time!")
                break
            case _:
                print("unimplemented!")
