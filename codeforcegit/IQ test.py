n = int(input())  # Number of elements
numbers = list(map(int, input().split()))  # List of numbers

# Create a list of the parity (0 if even, 1 if odd) for each number
parity = []
for num in numbers:
    parity.append(num % 2)
# Alternatively, you can use a list comprehension to create the parity list
# parity = [num % 2 for num in numbers]

# Check which parity is the minority and return its index + 1 (1-based indexing)
if parity.count(0) == 1:
    print(parity.index(0) + 1)
else:
    print(parity.index(1) + 1)
