#String - Not mutable:
str = "Omkar";
# print(str)
# str[1] = 'n'
# print(str)


#list - Mutable
listEx = [1,"Omkar",9.69]
# print(listEx)
# listEx[0] = 4
# print(listEx)


#tuples - Immutable
tupleEx = (4,"Omkar",9.69);
# print(tupleEx)
# tupleEx[2] = 6.99
# print(tupleEx)

#Dictionary - Mutable
dictionaryEx = {
    "rollno" : 1,
    "name": "Omkar",
    "Pointer": 9.69
}
# print(dictionaryEx)
# dictionaryEx["rollno"] = 4;
# print(dictionaryEx)


#More Complex List
complexList = [
    [4,8,14],
    (4,"Omkar"),
    {"rollno" : 1,
    "name": "Omkar",
    "Pointer": 9.69}
    ]

# print(complexList[2]["Pointer"])