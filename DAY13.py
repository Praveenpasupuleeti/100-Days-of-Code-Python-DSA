# -----------------------------------------------
# Day 13 - OOP Inheritance: Single, Multilevel, Multiple
# -----------------------------------------------

# --------------------------------
# Problem 1: Single Inheritance
# --------------------------------

class Animal:
    def speak(self):
        print("Generic Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Barking...")

print("Problem 1 - Single Inheritance")
d = Dog()
d.speak()
d.bark()


# --------------------------------
# Problem 2: Multilevel Inheritance
# --------------------------------

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class GraduateStudent(Student):
    def __init__(self, name, roll_no, specialization):
        super().__init__(name, roll_no)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Specialization: {self.specialization}")

print("\nProblem 2 - Multilevel Inheritance")
grad = GraduateStudent("Praveen", 101, "Data Science")
grad.display()


# --------------------------------
# Problem 3: Multiple Inheritance
# --------------------------------

class Programmer:
    def write_code(self):
        print("Writes code")

class Designer:
    def create_ui(self):
        print("Designs UI")

class TechLead(Programmer, Designer):
    def lead_team(self):
        print("Leads team")

print("\nProblem 3 - Multiple Inheritance")
lead = TechLead()
lead.write_code()
lead.create_ui()
lead.lead_team()
