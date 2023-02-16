def display(l):
    # TODO: do pretty print
    for _, item in enumerate(l):
        print(item)

def main():
    students = []
    courses = []

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

if __name__ == "__main__":
    main()
