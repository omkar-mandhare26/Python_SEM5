dic = {'a':7,'b':4,'c':3,'d':5,'e':2}

print(dic)
dictAsc = dict(sorted(dic.items(), key=lambda item: item[1]))
print(dictAsc)

dictDesc = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
print(dictDesc)
