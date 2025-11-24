class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class StudentManager:
    def __init__(self):
        self.filename = "students.txt"
        self.students = self.load_students()

    def load_students(self):
        data = {}
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    name, marks = line.strip().split(',')
                    data[name] = int(marks)
        except FileNotFoundError:
            pass  # If file doesn't exist, return empty dict
        return data

    def save_students(self):
        try:
            with open(self.filename, 'w') as f:
                for name, marks in self.students.items():
                    f.write(f"{name},{marks}\n")
        except Exception as e:
            print("Error writing file:", e)

    def add_student(self):
        try:
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            self.students[name] = marks
            self.save_students()
            print(f"Student '{name}' added.\n")
      
        except Exception as e:
            print(f"Error adding student: {e}\n")

    def view_students(self):
        if self.students:
            print("Student List:")
            for name, marks in self.students.items():
                print(f"{name}: {marks}")
            print()
        else:
            print("No students found.\n")

    def search_student(self):
        name = input("Enter name to search: ")
        if name in self.students:
            print(f"{name}: {self.students[name]}\n")
        else:
            print("Student not found.\n")

    def update_student(self):
        name = input("Enter name to update: ")
        if name in self.students:
            new_marks = int(input("Enter new marks: "))
            self.students[name] = new_marks
            self.save_students()
            print("Updated successfully.\n")
        else:
            print("Student not found.\n")

    def delete_student(self):
        name = input("Enter name to delete: ")
        if name in self.students:
            del self.students[name]
            self.save_students()
            print("Deleted successfully.\n")
        else:
            print("Student not found.\n")

    def find_topper(self):
        if self.students:
            topper = max(self.students, key=self.students.get)
            print(f"Topper: {topper} - {self.students[topper]}\n")
        else:
            print("No students to check.\n")

    def calculate_average(self):
        if self.students:
            avg = sum(self.students.values()) / len(self.students)
            print(f"Average marks: {avg:.2f}\n")
        else:
            print("No data.\n")

sm = StudentManager()

while True:
    print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Topper\n7. Average\n8. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        sm.add_student()
    elif choice == '2':
        sm.view_students()
    elif choice == '3':
        sm.search_student()
    elif choice == '4':
        sm.update_student()
    elif choice == '5':
        sm.delete_student()
    elif choice == '6':
        sm.find_topper()
    elif choice == '7':
        sm.calculate_average()
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")

