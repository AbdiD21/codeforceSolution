def can_reduce_to_one_element(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            return "NO"
    return "YES"

# Read all input at once
data = input().split()
t = int(data[0])
index = 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + n]))
    index += n
    results.append(can_reduce_to_one_element(arr))

# Output all results at once
print("\n".join(results))
