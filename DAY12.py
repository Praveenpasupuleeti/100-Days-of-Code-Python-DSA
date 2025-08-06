# ---------------------------------------
# Day 12 - OOP: Inheritance, Overriding, Encapsulation
# ---------------------------------------

# -----------------------------
# Problem 1: Single Inheritance
# -----------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):  # Inheriting from Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    # -------------------------------
    # Problem 2: Method Overriding
    # -------------------------------
    def display(self):
        super().display()  # Call parent class display
        print(f"Department: {self.department}")

print("Problem 1 & 2 - Inheritance and Method Overriding")
mgr = Manager("Ravi", 50000, "IT")
mgr.display()


# ----------------------------------------
# Problem 3: Encapsulation with Getters/Setters
# ----------------------------------------

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

    def get_balance(self):
        return self.__balance

print("\nProblem 3 - Encapsulation Example")
acc = BankAccount()
acc.set_balance(10000)
print("Balance (via getter):", acc.get_balance())

# Trying to access private variable directly (will fail)
try:
    print("Trying direct access:", acc.__balance)
except AttributeError:
    print("Direct access failed: Private variable")

# Access using name mangling (not recommended in practice)
print("Access via name mangling:", acc._BankAccount__balance)
