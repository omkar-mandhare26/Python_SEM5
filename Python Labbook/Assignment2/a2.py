str = "This is a string"
countDic = {}
for ch in str:
    if ch in countDic:
        countDic[ch]+=1
    else:
        countDic[ch] = 1

print(countDic)
