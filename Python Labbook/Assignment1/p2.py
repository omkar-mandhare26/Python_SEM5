salary = int(input("Enter Salary: "))
print(f"Salary is {salary}")

if salary <= 250000:
    print("Income Tax is 0")
elif salary <= 500000:
    print(f"Income Tax on {salary} is {(salary-250000)*0.1}")
else:
    t1 = 250000 * 0.1
    tax = ((salary-500000) * 0.2) + t1    
    print(f"Income Tax on {salary} is {tax}")