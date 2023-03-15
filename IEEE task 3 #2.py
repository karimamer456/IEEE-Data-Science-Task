s = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
result = ''
for c in s:
    if c in vowels:
        continue
    result += '.' + c

print(result)
