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