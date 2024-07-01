str = "This is a string"
str = str.lower()
count = 0
vowels = ['a','e','i','o','u']

for ch in str:
    if(ch in vowels):
        count+=1

print(count)