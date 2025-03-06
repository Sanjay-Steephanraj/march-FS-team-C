n =input("Enter a string: ")
vowel = ['a','e','i','o','u']
count = 0
for i in n:
    if i in vowel:
        count += 1
print("count of vowels", count)