students = []

def add_student():
    name = input("Enter name >> ").title()
    age = int(input("Enter age >> "))
    grade = input("Enter grade >> ").upper()
    students.append({
        "name": name,
        "age": age,
        "grade": grade
    })
    print(f"\n✅ {name} added successfully!")

def view_students():
    if len(students) == 0:
        print("\n❌ No students found!")
        return
    print("\n======= All Students =======")
    for index, student in enumerate(students, 1):
        print(f"{index}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print("============================")

def search_student():
    name = input("Enter name to search >> ").title()
    for student in students:
        if student["name"] == name:
            print(f"\n✅ Found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return
    print(f"\n❌ {name} not found!")

def delete_student():
    name = input("Enter name to delete >> ").title()
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"\n✅ {name} deleted successfully!")
            return
    print(f"\n❌ {name} not found!")

def main():
    while True:
        print("\n======= Student Database =======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Quit")
        print("================================")
        
        choice = int(input(">>> "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Goodbye Baanbil! 👋")
            break
        else:
            print("❌ Invalid option!")

main()
