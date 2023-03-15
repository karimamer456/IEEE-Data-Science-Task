s = input()

# Keep track of the index of the next letter to match
next_letter_index = 0

# Iterate through each letter in s
for letter in s:
    # If the current letter matches the next letter to match, move on to the next letter to match
    if letter == "hello"[next_letter_index]:
        next_letter_index += 1
        # If we have matched all five letters, Vasya managed to say hello
        if next_letter_index == 5:
            print("YES")
            break

# If we made it through the loop without finding "hello", Vasya didn't manage to say hello
else:
    print("NO")