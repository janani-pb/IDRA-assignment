
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"


students = []


def add_student():
    try:
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(name, marks)
        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid marks.")


def view_students():

    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student Details ---")

    for student in students:
        student.display()
        print("Grade:", student.grade())
        print("----------------------")


def save_students():

    file = open("students.txt", "w")

    for student in students:
        file.write(student.name + "," + str(student.marks) + "\n")

    file.close()


while True:

    print("\n===== Student Grade Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save Students")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            save_students()
            print("Students saved successfully!")

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a number.")

