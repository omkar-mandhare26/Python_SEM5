str = "Labbook"
occurrences = {}
newStr = ""

for ch in str:
    if ch in occurrences:
        occurrences[ch] += 1
        newStr += '$'
    else:
        occurrences[ch] = 1
        newStr += ch

print(str)
print(newStr)