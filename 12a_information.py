print("\n\n\t\t *** Student Information Management Expert System ***\n")

# Define an empty dictionary to store student records
student_records = {}

# Function to add or update a student record
def add_update_student():
    student_id = input("Enter the student ID: ")
    name = input("Enter the student's name: ")
    program = input("Enter the student's program: ")
    year = input("Enter the student's year of study: ")
    gpa = input("Enter the student's GPA: ")

    student_records[student_id] = {
        "Name": name,
        "Program": program,
        "Year of Study": year,
        "GPA": gpa
    }

    print("Student record added/updated successfully.")

# Function to retrieve a student record
def retrieve_student():
    student_id = input("Enter the student ID to retrieve the record: ")
    student_info = student_records.get(student_id)

    if student_info:
        print("\n\t---------------------- Student Information -----------------------\n")
        for field, value in student_info.items():
            print("\t" + field + ": " + value)
        print("\n\t-----------------------------------------------------------------")
    else:
        print("Student record not found.")

# Function to delete a student record
def delete_student():
    student_id = input("Enter the student ID to delete the record: ")
    if student_records.pop(student_id, None):
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")

# Main menu loop
while True:
    print("\n\t------------------------- Main Menu ------------------------------")
    print("\t1. Add or Update a student record")
    print("\t2. Retrieve a student record")
    print("\t3. Delete a student record")
    print("\t4. Exit")
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_update_student()
    elif choice == "2":
        retrieve_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
