def solve():
    x1, x2, x3 = map(int, input().split())
    arr = sorted([x1, x2, x3])
    print(arr[2] - arr[0])

solve()
