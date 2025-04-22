n = int(input())
teams = []
for i in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))

count = 0
for j in range(n):
    for k in range(n):
        if j != k:
            if teams[j][0] == teams[k][1]:
                count += 1
   
print(count)
