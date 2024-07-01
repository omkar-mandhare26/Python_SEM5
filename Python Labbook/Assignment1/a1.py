n = 5687
temp = n
sum = 0

while temp>0:
    rem = temp%10
    sum += rem
    temp = int(temp/10)

print(f"Sum of {n} is {sum}")
