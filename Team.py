# Read the number of problems
n = int(input())

# Initialize the counter for problems they will solve
solve_count = 0

# Loop through each problem
for i in range(n):
    # Read the opinions of Petya, Vasya, and Tonya (each a 0 or 1)
    p, v, t = map(int, input().split())

    # If at least two of them are sure about the solution, increment the counter
    if p + v + t >= 2:
        solve_count += 1

print(solve_count)
