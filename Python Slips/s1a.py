list = [4,4,14,8]
# n = int(input("Enter No of Elements: "))
# for i in range(0,n):
#     e = int(input(f"Enter Element {i+1}: "))
#     list.append(e)

print(f"Before Removing Duplicates: {list}")

# Manual Approach
# for i in range(len(list)-1):
#     k = i+1
#     tempList = list[k:]
#     checkN = list[i]
#     if checkN in tempList: list.remove(checkN)

# Easy Approach
# set = set(list)
# newList = []
# for n in set:
#     newList.append(n)

# Clg Approach
newList = []
for i in list:
    if i not in newList: newList.append(i)


print(f"After Removing Duplicates: {newList}")