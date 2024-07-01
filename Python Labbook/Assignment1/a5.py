n = int(input("Enter any integer: "))

revStr = str(n)[::-1]
revN = int(revStr)

if revN == n:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")