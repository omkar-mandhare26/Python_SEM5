num = str(input("Enter any integer: "))

evenCount = 0
oddCount = 0
zeroCount = 0

for n in num:
    t = int(n)
    if t == 0: zeroCount+=1
    elif t % 2 == 0: evenCount+=1
    elif t % 2: oddCount+=1

print(f"Even Count: {evenCount}")
print(f"Odd Count: {oddCount}")
print(f"Zero Count: {zeroCount}")