from .domains import Major
import textwrap

def inputs(major: Major):
    print(textwrap.dedent("""\
        welcome to the student management system.
        what do you want to do?
            1 - input students info
            2 - input courses info
            3 - input marks
        """))

    while True:
        print(f"proudly managing {len(major.students)} students and {len(major.courses)} courses!")

        choice = int(input("choice: "))
        print()

        match choice:
            case 1:
                major.add_student()
            case 2:
                major.add_course()
            case 3:
                if not major.students:
                    print("there are no students!")
                elif not major.courses:
                    print("there are no courses!")
                else:
                    major.add_mark()
            case 8: 
                print("see you next time!")
                break
            case _:
                print("unimplemented!")
