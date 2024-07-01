n = int(input("Enter any integer: "))
lastDigit = n % 10

revStr = str(n)[::-1]
revN = int(revStr)
firstDigit = revN % 10

print(f"Sum of first and last digits of {n}: {firstDigit + lastDigit}")