n = int(input("Enter Stating num: "))
m = int(input("Enter Ending num: "))

for i in range(1,11):
    for j in range(n,m+1):
        print(i*j,end="\t")
    
    print()