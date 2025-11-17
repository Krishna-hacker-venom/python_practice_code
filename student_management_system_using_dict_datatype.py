# Student Management System

students = {}

while True:
    print("\nStudent Management System Menu:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Search Student")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # ------------------------ ADD STUDENT ------------------------
    if choice == '1':
        sid = input("Enter Student ID: ")

        if sid in students:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")

            students[sid] = {"name": name, "age": age, "grade": grade}
            print(f"Student {name} added successfully!")

    # ------------------------ UPDATE STUDENT ------------------------
    elif choice == '2':
        sid = input("Enter Student ID to update: ")

        if sid in students:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Grade")

            update_choice = input("Enter option (1-3): ")

            if update_choice == '1':
                new_name = input("Enter new name: ")
                students[sid]["name"] = new_name
                print("Name updated successfully!")

            elif update_choice == '2':
                new_age = input("Enter new age: ")
                students[sid]["age"] = new_age
                print("Age updated successfully!")

            elif update_choice == '3':
                new_grade = input("Enter new grade: ")
                students[sid]["grade"] = new_grade
                print("Grade updated successfully!")

            else:
                print("Invalid option!")

        else:
            print("Student ID not found!")

    # ------------------------ DELETE STUDENT ------------------------
    elif choice == '3':
        sid = input("Enter Student ID to delete: ")

        if sid in students:
            del students[sid]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # ------------------------ VIEW ALL STUDENTS ------------------------
    elif choice == '4':
        if not students:
            print("No students available!")
        else:
            print("\n--- All Students ---")
            for sid, details in students.items():
                print(f"ID: {sid}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")

    # ------------------------ SEARCH STUDENT ------------------------
    elif choice == '5':
        sid = input("Enter Student ID to search: ")

        if sid in students:
            print("\nStudent Found:")
            print(f"ID: {sid}")
            print(f"Name: {students[sid]['name']}")
            print(f"Age: {students[sid]['age']}")
            print(f"Grade: {students[sid]['grade']}")
        else:
            print("Student not found!")

    # ------------------------ EXIT PROGRAM ------------------------
    elif choice == '6':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
