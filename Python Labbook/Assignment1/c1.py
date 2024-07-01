n = 4  # Number of rows

for i in range(1, n+1):
    # Print leading spaces
    print(" " * (n-i), end="")
    
    # Print the ascending numbers
    for j in range(1, i+1):
        print(j, end="")
    
    # Print the descending numbers
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    print()
