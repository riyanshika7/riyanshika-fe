
# A simple Student Record Manager using file handling.
import os

DATA_FILE = "students.txt"

def add_student():
    """Adds a new student record to the file."""
    print("\n--- Add New Student ---")
    name = input("Enter Student Name: ").strip()
    roll = input("Enter Roll Number: ").strip()
    marks = input("Enter Marks: ").strip()

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{roll},{marks}\n")

    print("Student record added successfully!")

def list_students():
    """Displays all student records."""
    print("\n--- Student Records ---")

    if not os.path.exists(DATA_FILE):
        print("No records found.")
        return

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

        if not lines:
            print("No records found.")
            return

        print("{:<20} {:<10} {:<6}".format("Name", "Roll", "Marks"))
        print("-" * 40)

        for line in lines:
            name, roll, marks = line.strip().split(",")
            print("{:<20} {:<10} {:<6}".format(name, roll, marks))

def search_student():
    """Searches for a student by roll number."""
    print("\n--- Search Student ---")
    roll_search = input("Enter Roll Number to search: ").strip()

    found = False

    if not os.path.exists(DATA_FILE):
        print("No records found.")
        return

    with open(DATA_FILE, "r") as file:
        for line in file:
            name, roll, marks = line.strip().split(",")
            if roll == roll_search:
                print("\nStudent Found:")
                print(f"Name  : {name}")
                print(f"Roll  : {roll}")
                print(f"Marks : {marks}")
                found = True
                break

    if not found:
        print("Student not found.")

def main():
    """Main menu loop for the program."""
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. List All Students")
        print("3. Search Student by Roll")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

main()
