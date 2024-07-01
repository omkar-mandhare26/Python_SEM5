# is : True if the operands are identical
# is not : True if the operands are not identical

#Having same memory
# num1 = 5;
# num2 = num1;
# if(num1 is num2):
#     print("Both are identical")
# else:
#     print("Both are not indentical")

#Having same value but immutable type
# num1 = 5;
# num2 = 5;
# if(num1 is num2):
#     print("Both are identical")
# else:
#     print("Both are not indentical")
#Output is true because it is immutable

#Comparing same value but different memory but this time its mutable:
list1 = [1,2,3]
# list2 = list1
list2 = [1,2,3]
if(list1 is list2):
    print("Both Lists are identical")
else:
    print("Both Lists are not indentical")
#Returns false as list are mutable 