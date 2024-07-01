n = 28
sum = 0

for i in range(1,n-1):
    if n % i == 0:
        sum += i 

if sum == n:
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is not a Perfect Number")