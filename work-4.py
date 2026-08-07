
import csv

file_name = "expenses.csv"


def add_expense():
    try:
        date = input("Enter date: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        note = input("Enter note: ")

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([date, category, amount, note])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    try:
        file = open(file_name, "r")
        reader = csv.reader(file)

        total = 0

        print("\n--- Expenses ---")

        for row in reader:
            print("Date:", row[0])
            print("Category:", row[1])
            print("Amount:", row[2])
            print("Note:", row[3])
            print("----------------")

            total = total + float(row[2])

        print("Total Amount Spent:", total)

        file.close()

    except FileNotFoundError:
        print("No expenses found.")


def category_summary():
    try:
        file = open(file_name, "r")
        reader = csv.reader(file)

        categories = {}

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in categories:
                categories[category] = categories[category] + amount
            else:
                categories[category] = amount

        print("\n--- Category Wise Summary ---")

        for category in categories:
            print(category, ":", categories[category])

        file.close()

    except FileNotFoundError:
        print("No expenses found.")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Wise Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
