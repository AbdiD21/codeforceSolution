n = int(input())
numbers = list(map(int, input().split()))

parity = []
for num in numbers:
    parity.append(num % 2)

if parity.count(0) == 1:
    print(parity.index(0) + 1)
else:
    print(parity.index(1) + 1)
