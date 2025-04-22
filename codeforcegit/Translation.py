s = input().strip()
t = input().strip()

# Check if the second word is the reverse of the first word
if t == s[::-1]:
    print("YES")
else:
    print("NO")
