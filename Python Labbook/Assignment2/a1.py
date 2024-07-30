# ! Wrongly Done
# list = [2, 45, 90, 45, 6]
# flag = True

# for i in range(0,len(list)):
#     if list[i] in list[i+1:]:
#         flag = False
    
# print(flag)

#First Apporach
# flag = True
# list = []
# for i in range(5):
#     n = int(input(f"Enter Data {i+1}: "))
#     if(n in list): 
#         flag = False

#     list.append(n)

# if flag:
#     print("ALL UNIQUE")
# else:
#     print("DUPLICATES")

#Second Approach
list = []
for i in range(5):
    n = int(input(f"Enter Data {i+1}: "))
    list.append(n)

set = set(list)
if len(set)<len(list):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")