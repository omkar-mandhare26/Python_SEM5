n = 153
temp = n
sum = 0

while temp>0:
    rem = temp%10
    sum += pow(rem,3)
    temp = int(temp/10)

if sum == n:
    print(f"{n} is Armstrong")
else:
    print(f"{n} is not an Armstrong")

