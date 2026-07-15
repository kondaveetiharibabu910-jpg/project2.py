students = {}

def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    students[roll_no] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    print("Student added successfully.")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for roll_no, details in students.items():
            print("----------------------")
            print("Roll No:", roll_no)
            print("Name:", details["name"])
            print("Age:", details["age"])
            print("Marks:", details["marks"])

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")