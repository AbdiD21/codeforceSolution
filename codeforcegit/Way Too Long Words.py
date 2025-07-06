n = int(input())

words = []
for count in range(n):
    word = input()
    words.append(word)
# words = [input() for count in range(n)]

results = []
for word in words:
    if len(word) > 10:
        abbreviated = word[0] + str(len(word) - 2) + word[-1]
        results.append(abbreviated)
    else:
        results.append(word)

print("\n".join(results))
