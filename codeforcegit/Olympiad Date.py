t = int(input())
required = {0: 3, 1: 1, 3: 1, 2: 2, 5: 1}
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 5: 0}
    res = 0
    for i in range(n):
        num = a[i]
        if num in required:
            counts[num] += 1
        # Check if all required counts are met
        met = True
        for d in required:
            if counts[d] < required[d]:
                met = False
                break
        if met:
            res = i + 1
            break
    print(res)



'''
def can_form_date(drawn_digits):
    target_digits = [0, 1, 0, 3, 2, 0, 2, 5]  # target for "01.03.2025"
    from collections import Counter

    # Count the necessary digits
    target_count = Counter(target_digits)
    current_count = Counter()
    
    for index, digit in enumerate(drawn_digits):
        current_count[digit] += 1
        
        # Check if we can form the target date
        if all(current_count[d] >= target_count[d] for d in target_count):
            return index + 1  # return 1-based index
    
    return 0  # return 0 if we cannot form the date


def olympiad_date(test_cases):
    results = []
    for n, digits in test_cases:
        result = can_form_date(digits)
        results.append(result)
    return results


# Example Usage
t = int(input())  # number of test cases
test_cases = []
for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    test_cases.append((n, digits))

results = olympiad_date(test_cases)
for res in results:
    print(res)
'''
