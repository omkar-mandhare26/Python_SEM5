# Write a Python program to calculate sum of digit of given input number
n = 45683
sum = 0
temp = n
while temp>0:
    r = temp%10
    sum += r
    temp = temp//10

print(f"Sum of {n}: {sum}")

# Write a Python program to check given input number is perfect or not
n = 28
sum = 0
for i in range(1,n-1):
    if n%i ==0: sum += i

if sum == n:
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is not a Perfect Number")

# Write a python script which accept 5 integer value and print duplicate value entered are duplicate otherwise prints all unique
flag = True
list = []
for i in range(5):
    n = int(input(f"Enter Data {i+1}: "))
    if n in list : flag = False
    list.append(n)

if flag:
    print("ALL UNIQUE")
else:
    print("DUPLICATES")

# Write a Python program to check if the given key exits in a dictionary.
dict = {'A':45, 'B': 35,'C': 78}
keyToCheck = 'A'

if keyToCheck in dict.keys():
    print("Key exists in the dictionary")
else:
    print("Key does not exists in the dictionary")

# Write a Python program to calculate factorial of given number using function.
num = 5

def factorial(n):
    if (n==1 or n==0): return 1
    else: return n * factorial(n-1) 

print(f"Factorial of {num}: {factorial(num)}")