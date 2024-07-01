cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))

if sp > cp:
    print(f"Seller made Profit of {sp-cp}")
else:
    print(f"Seller made Loss of {cp-sp}")
