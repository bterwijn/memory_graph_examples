import json


class Student:
    total_students = 0

    def __init__(
        self,
        name,
        roll_number,
        age,
        m1,
        m2,
        m3,
        m4,
        m5,
    ):
        Student.total_students += 1
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.marks = {
            "maths": m1,
            "physics": m2,
            "english": m3,
            "computer": m4,
            "chemistry": m5,
        }

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError
        else:
            self._age = value

    @classmethod
    def no_of_students(cls):
        return cls.total_students

    def percentage(self):
        total = 0

        for markkeys in self.marks:
            total = total + self.marks[markkeys]

        return total / 5

    def grade(self):
        per = self.percentage()

        if per > 90:
            return "A"
        elif per <= 90 and per >= 75:
            return "B"
        elif per < 75 and per >= 60:
            return "C"
        else:
            return "D"


class CollegeStudent(Student):
    def __init__(
        self,
        name,
        roll_number,
        age,
        m1,
        m2,
        m3,
        m4,
        m5,
        branch,
    ):
        super().__init__(
            name,
            roll_number,
            age,
            m1,
            m2,
            m3,
            m4,
            m5,
        )
        self.branch = branch

    def display(self):
        print("NAME=", self.name)
        print("AGE=", self.age)
        print("ROLL NUMBER=", self.roll_number)

        for key in self.marks.keys():
            print(key, "=", self.marks[key])

        print("GRADE=", self.grade())
        print("PERCENTAGE=", self.percentage())
        print("BRANCH =", self.branch)


Subjects = (
    "maths",
    "physics",
    "chemistry",
    "english",
    "computer",
)

Students = []

s1 = CollegeStudent(
    "Riddhim",
    24,
    18,
    98,
    99,
    99,
    99,
    99,
    "AIML",
)

s2 = CollegeStudent(
    "Aman",
    25,
    19,
    85,
    80,
    90,
    95,
    88,
    "CSE",
)

Students.append(s1)
Students.append(s2)


def add_student():
    name = input("ENTER A NAME")
    roll_number = int(input("ENTER ROLL NUMBER"))
    age = int(input("ENTER AGE"))
    M1 = int(input("ENTER MARKS IN MATHS"))
    M2 = int(input("ENTER MARKS IN PHYSICS"))
    M3 = int(input("ENTER MARKS IN ENGLISH"))
    M4 = int(input("ENTER MARKS IN COMPUTER"))
    M5 = int(input("ENTER MARKS IN CHEMISTRY"))
    branch = input("ENTER BRANCH")

    s = CollegeStudent(
        name,
        roll_number,
        age,
        M1,
        M2,
        M3,
        M4,
        M5,
        branch,
    )

    Students.append(s)


def delete_student():
    found = False
    i = int(input("ENTER THE ROLL NUMBER OF THE STUDENT"))

    for student in Students:
        if student.roll_number == i:
            Students.remove(student)
            found = True
            break

    if found == False:
        raise ValueError("Student Not Found")


def search_student():
    found = False
    i = int(input("ENTER THE ROLL NUMBER OF THE STUDENT"))

    for student in Students:
        if student.roll_number == i:
            student.display()
            found = True
            break

    if found == False:
        raise ValueError("Student Not Found")


def find_topper():
    try:
        topper = Students[0]

        for student in Students:
            if topper.percentage() < student.percentage():
                topper = student

        topper.display()

    except Exception:
        print("School is bankrupt and there are no students")


def class_average():
    if not Students:
        print("CLASS IS EMPTY")
    else:
        total = 0

        for student in Students:
            total += student.percentage()

        avg = total / len(Students)
        print("CLASS AVERAGE=", avg)


def sort_students_by_percentage():
    temp = Students.copy()
    rank = []

    while len(temp) != 0:
        topper = temp[0]

        for student in temp:
            if topper.percentage() < student.percentage():
                topper = student

        rank.append(topper)
        temp.remove(topper)

    x = 1

    for student in rank:
        print(f"RANK {x}=", student.name)
        x += 1


def display_all_students():
    for student in Students:
        student.display()


def update_student():
    found = False

    i = int(
        input(
            "ENTER THE ROLL NUMBER OF THE STUDENT "
            "WHOSE INFORMATION HAS TO BE UPDATED"
        )
    )

    for student in Students:
        if student.roll_number == i:
            found = True

            x = int(
                input(
                    """CHANGE:
                    1.Age
                    2.Marks
                    3.Branch
                    """
                )
            )

            match x:
                case 1:
                    student.age = int(input("ENTER AGE"))

                case 2:
                    i = input(
                        "WHICH SUBJECT MARKS IS TO BE CHANGED"
                    )
                    student.marks[i] = int(
                        input("ENTER NEW MARKS")
                    )

                case 3:
                    student.branch = input("ENTER NEW BRANCH")

            break

    if found == False:
        raise ValueError("STUDENT NOT FOUND")
    else:
        print("Student updated successfully")


def save_data():
    temp = []

    for student in Students:
        student_dict = {
            "name": student.name,
            "roll_number": student.roll_number,
            "age": student.age,
            "marks": student.marks,
            "branch": student.branch,
        }

        temp.append(student_dict)

    try:
        with open("students.json", "w") as file:
            json.dump(temp, file)

    except Exception as e:
        print("Saving failed:", e)


def load_data():
    try:
        with open("students.json", "r") as file:
            temp = json.load(file)

        Students.clear()

        for student in temp:
            s = CollegeStudent(
                student["name"],
                student["roll_number"],
                student["age"],
                student["marks"]["maths"],
                student["marks"]["physics"],
                student["marks"]["english"],
                student["marks"]["computer"],
                student["marks"]["chemistry"],
                student["branch"],
            )

            Students.append(s)

    except Exception as e:
        print("Loading failed:", e)


load_data()

while True:
    choice = str(
        input(
            """==== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Delete Student
3. Search Student
4. Update Student
5. Display All Students
6. Save Data
7. Load Data
8. Exit

Enter Choice:"""
        )
    )

    if choice == "8":
        save_data()
        break

    menu = {
        "1": add_student,
        "2": delete_student,
        "3": search_student,
        "4": update_student,
        "5": display_all_students,
        "6": save_data,
        "7": load_data,
    }

    if choice in menu:
        menu[choice]()
