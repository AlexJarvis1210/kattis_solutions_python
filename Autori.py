word = input()
n = 0

for letter in range(len(word)):
    if word[letter] == "a":
        suffix = word[n:]
        print(suffix)
        break
    else:
        n += 1