students = {}

def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")

    marks = []
    for i in range(5):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    percentage = sum(marks) / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    students[roll_no] = {
        "name": name,
        "roll_no": roll_no,
        "percentage": percentage,
        "grade": grade
    }

    print("Added Successfully...")


def view_students():
    if not students:
        print("No student records available.")
    else:
        print("\n***🎓 All Students 🎓***")

        for roll_no, details in students.items():
            print("\nRoll Number:", roll_no)
            print("Name:", details["name"])
            print("Roll No:", details["roll_no"])
            print("Percentage:", details["percentage"])
            print("Grade:", details["grade"])


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    student = students.get(roll_no)

    if student:
        print("\nStudent Details:")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Percentage:", student["percentage"])
        print("Grade:", student["grade"])
    else:
        print("Student not found...")


def update_student():
    roll_no = input("Enter Roll Number to update marks: ")

    student = students.get(roll_no)

    if student:
        new_marks = float(input("Enter New Marks: "))

        student.update({"marks": new_marks})

        print("Marks updated successfully...")
    else:
        print("Student not found...")


def remove_student():
    roll_no = input("Enter Roll Number to remove: ")

    removed_student = students.pop(roll_no, None)

    if removed_student:
        print("Student removed successfully...")
    else:
        print("Student not found...")


while True:
    print("\n***🎓 Student Management System 🎓***")
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        print("Exiting Student Management System ...")
        break

    else:
        print("Invalid choice...")