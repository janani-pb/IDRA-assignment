students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")

        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            print("----------------------")


def search_student():
    search = input("Enter Student ID or Name: ")

    found = False

    for student in students:
        if student["ID"] == search or student["Name"].lower() == search.lower():
            print("\nStudent Found!")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            found = True

    if not found:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:
            print("Leave blank if you don't want to change a value.")

            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            course = input("Enter new Course: ")
            marks = input("Enter new Marks: ")

            if name != "":
                student["Name"] = name

            if age != "":
                student["Age"] = age

            if course != "":
                student["Course"] = course

            if marks != "":
                student["Marks"] = marks

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")