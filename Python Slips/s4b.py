class Employee:
    def __init__(self):
        self.id = None
        self.name = None
        self.dept = None
        self.salary = None

    def acceptEmpDetails(self):
        self.id = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.dept = input("Enter Department Name: ")
        self.salary = int(input("Enter Employee Salary: "))

    def displayEmpDetails(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.dept}")
        print(f"Employee Salary: {self.salary}")

    def getSalary(self): return self.salary

class Manager(Employee):
    def __init__(self):
        self.bonus = 0
        super().__init__()

    def getMangerDetails(self):
        super().acceptEmpDetails()
        self.bonus = int(input("Enter Bonus Amount: "))

    def displayManagerDetails(self):
        super().displayEmpDetails()
        print(f"Manager Bonus: {self.bonus}")

    def getFinalSalary(self):
        return super().getSalary() + self.bonus

n = int(input("Enter No of objects: "))

managers = []

for i in range(0,n):
    Manager_Object = Manager()
    print(f"\nEnter Details for Manager {i+1}: ")
    Manager_Object.getMangerDetails()
    managers.append(Manager_Object)

# Find Maximum Salary
maxSal = managers[0].getFinalSalary()
k = 0
for i in range(1,n):
    sal = managers[i].getFinalSalary()
    if maxSal < sal: 
        maxSal = sal
        k = i

print("\nManager With Highest Salary")
managers[k].displayManagerDetails()