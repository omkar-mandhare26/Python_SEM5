price = int(input("Enter Total Price: "))
print(price)

tenPriceNotes = int(price/10)
price %= 10;

fivePriceNotes = int(price/5)
price %= 5

print(f"Amt Withdrawn in cash is {tenPriceNotes} Rs.10 Notes, {fivePriceNotes} Rs.5 Notes, {price} Rs.1 Notes")