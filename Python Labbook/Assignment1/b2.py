binaryNo = str(input("Enter binary no: "))


decimalNo = 0
binaryStr = binaryNo[::-1]
for i in range(len(binaryStr)):
    if binaryStr[i] == '1':
        decimalNo += 2 ** i

print(decimalNo)