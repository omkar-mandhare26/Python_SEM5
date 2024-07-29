str = "This is a string"
str = str.lower()
vowelCount = 0
consonantCount = 0
vowels = ['a','e','i','o','u']

for ch in str:
    if(ch in vowels): vowelCount+=1
    else: consonantCount+=1

print(f"Vowel Count: {vowelCount}")
print(f"Consonant Count: {consonantCount}")