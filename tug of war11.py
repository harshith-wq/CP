from itertools import combinations
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
k = n // 2

# Split the array into two halves
mid = n // 2
left = arr[:mid]
right = arr[mid:]

# Store subset sums grouped by number of selected elements
left_sums = [[] for _ in range(len(left) + 1)]
right_sums = [[] for _ in range(len(right) + 1)]

for mask in range(1 << len(left)):
    count = 0
    s = 0
    for i in range(len(left)):
        if mask & (1 << i):
            count += 1
            s += left[i]
    left_sums[count].append(s)

for mask in range(1 << len(right)):
    count = 0
    s = 0
    for i in range(len(right)):
        if mask & (1 << i):
            count += 1
            s += right[i]
    right_sums[count].append(s)

# Sort right-side sums for binary search
for sums in right_sums:
    sums.sort()

answer = float('inf')

# Try selecting k people
for lc in range(len(left) + 1):
    rc = k - lc

    if 0 <= rc <= len(right):
        for s1 in left_sums[lc]:
            target = total / 2 - s1
            sums = right_sums[rc]

            pos = bisect_left(sums, target)

            if pos < len(sums):
                selected = s1 + sums[pos]
                answer = min(answer, abs(total - 2 * selected))

            if pos > 0:
                selected = s1 + sums[pos - 1]
                answer = min(answer, abs(total - 2 * selected))

# For odd N, selecting k+1 people is also valid.
if n % 2 == 1:
    k += 1

    for lc in range(len(left) + 1):
        rc = k - lc

        if 0 <= rc <= len(right):
            for s1 in left_sums[lc]:
                target = total / 2 - s1
                sums = right_sums[rc]

                pos = bisect_left(sums, target)

                if pos < len(sums):
                    selected = s1 + sums[pos]
                    answer = min(answer, abs(total - 2 * selected))

                if pos > 0:
                    selected = s1 + sums[pos - 1]
                    answer = min(answer, abs(total - 2 * selected))

print(answer)
