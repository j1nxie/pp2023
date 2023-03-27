from .domains import Major
from . import input as ip
from . import output as op
import textwrap
import sys
import os

def main():
    major = Major([], [])

    print(textwrap.dedent("""\
        welcome to the student management system.
        what do you want to do?
            1 - input information
            2 - output information
            3 - exit
        """))

    while True:
        print(f"proudly managing {len(major.students)} students and {len(major.courses)} courses!")

        choice = int(input("choice: "))
        print()

        match choice:
            case 1:
                ip.inputs(major)
            case 2:
                op.outputs(major)
            case 3:
                print("see you next time!")
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
