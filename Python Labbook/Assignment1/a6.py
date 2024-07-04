n = int(input("Enter any integer: "))
revStr = str(n)[::-1]

lastDigit = n % 10
revN = int(revStr)
firstDigit = revN % 10

print(f"Sum of first and last digits of {n}: {firstDigit + lastDigit}")