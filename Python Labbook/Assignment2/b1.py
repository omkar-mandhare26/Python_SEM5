def ConcatString(str):
    if len(str) == 1:
        return None
    elif len(str) == 2:
        return str + str
    else:
        return str[:2] + str[-2:]

sentence = "O"    
newStr = ConcatString(sentence)

if newStr:
    print(f"New String: {newStr}")
else:
    print("Empty String")