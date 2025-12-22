# Student Management System

FILE_NAME = "students.txt"

def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                sid, name, dept, cgpa = line.strip().split(",")
                students.append({
                    "id": sid,
                    "name": name,
                    "dept": dept,
                    "cgpa": cgpa
                })
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['dept']},{s['cgpa']}\n")


def add_student(students):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    cgpa = input("Enter CGPA: ")

    students.append({
        "id": sid,
        "name": name,
        "dept": dept,
        "cgpa": cgpa
    })
    save_students(students)
    print("✅ Student added successfully!")


def view_students(students):
    if not students:
        print("❌ No student records found.")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Dept: {s['dept']} | CGPA: {s['cgpa']}")


def search_student(students):
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("🎯 Student Found:")
            print(s)
            return
    print("❌ Student not found.")


def update_student(students):
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("New Name: ")
            s["dept"] = input("New Department: ")
            s["cgpa"] = input("New CGPA: ")
            save_students(students)
            print("✅ Student updated successfully!")
            return
    print("❌ Student not found.")


def delete_student(students):
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("🗑 Student deleted successfully!")
            return
    print("❌ Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
