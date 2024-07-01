str = "This is a string"
newstr = ""
for i in range(len(str)):
    if(i%2==0):
        newstr += str[i]

print(newstr)