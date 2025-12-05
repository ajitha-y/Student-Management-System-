class StudentManagement:
    def __init__(self, filename="Student.txt"):
        self.filename = filename

    def add_student(self):
        try:
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            with open(self.filename, "a") as f:
                f.write(f"{sid},{name},{marks}\n")
            print("Student Added Successfully")
        except Exception as e:
            print("Error:", e)

    def view_students(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    sid, name, marks = line.strip().split(",")
                    print(f"ID: {sid} | Name: {name} | Marks: {marks}")
        except FileNotFoundError:
            print("No student file found")

    def search_student(self):
        sid = input("Enter ID to search: ")
        found = False
        with open(self.filename, "r") as f:
            for line in f:
                if line.startswith(sid + ","):
                    print("Student Found:", line.strip())
                    found = True
        if not found:
            print("Student Not Found")

    def update_delete_student(self):
        sid = input("Enter ID to Update/Delete: ")
        choice = input("Type U for Update or D for Delete: ").upper()
        lines = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            for line in lines:
                if line.startswith(sid + ","):
                    if choice == "U":
                        name = input("New Name: ")
                        marks = input("New Marks: ")
                        f.write(f"{sid},{name},{marks}\n")
                        print("Updated Successfully")
                    elif choice == "D":
                        print("Deleted Successfully")
                    continue
                f.write(line)

    def calculate_avg_topper(self):
        students = []
        with open(self.filename, "r") as f:
            for line in f:
                sid, name, marks = line.strip().split(",")
                students.append(float(marks))
        if students:
            avg = sum(students) / len(students)
            topper = max(students)
            print("Average:", avg)
            print("Topper Marks:", topper)









    








