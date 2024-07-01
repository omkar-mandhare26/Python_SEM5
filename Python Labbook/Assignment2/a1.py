#Wrongly Done
list = [2, 45, 90, 45, 6]
flag = True

for i in range(0,len(list)):
    if list[i] in list[i+1:]:
        flag = False
    
print(flag)