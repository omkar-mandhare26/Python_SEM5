tuple = ("S","t","r","i","n","g")
tupleStr = str(tuple)
print(tupleStr)
print(type(tupleStr))

#Other Ans
str = ""
for ch in tuple:
    str += ch

print(str)