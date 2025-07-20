n, m, a = map(int, input().split())
tiles = ((n + a - 1) // a) * ((m + a - 1) // a)
print(tiles)

# Time complexity: O(1)
# Space complexity: O(1)