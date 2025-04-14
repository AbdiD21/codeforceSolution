

t = int(input())
for count in range(t):
    n = int(input())
    s = input()

    completed_tasks = set()
    last_task = ''
    suspicious = False

    for task in s:
        if task != last_task:
            if task in completed_tasks:
                suspicious = True
                break
            completed_tasks.add(task)
        last_task = task

    if suspicious:
        print("NO")
    else:
        print("YES")

