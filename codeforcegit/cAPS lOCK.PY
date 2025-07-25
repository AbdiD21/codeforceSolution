word = input()

if word.isupper():
    print(word.lower())
elif len(word) > 1 and word[1:].isupper():
    print(word[0].upper() + word[1:].lower())
elif len(word) == 1 and word.islower():
    print(word.upper())
else:
    print(word)
