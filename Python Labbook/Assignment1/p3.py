x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

if x>0 and y>0:
    print("First Quadrant")
elif x>0 and y<0:
    print("Second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
elif x<0 and y>0:
    print("Fourth Quadrant")