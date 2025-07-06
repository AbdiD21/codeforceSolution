n = int(input())
#words = [input() for _ in range(n)]
words = []
for _ in range(n):
    word = input()
    words.append(word)

results = []
for word in words:
    if len(word) > 10:
        short = word[0] + str(len(word) - 2) + word[-1]
        results.append(short)
    else:
        results.append(word)

print("\n".join(results))


" Way Too Long Words "