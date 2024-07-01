n = int(input("Enter any integer: "))

for i in range(1,n):
    flag = True
    for j in range(2,i-1):
        if i % j == 0:
            flag = False
    
    if flag:
        print(i)