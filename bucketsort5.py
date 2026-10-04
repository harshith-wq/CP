import sys

data = sys.stdin.read().split()

n = int(data[0])
arr = list(map(float, data[1:n + 1]))

# Create n buckets
buckets = [[] for _ in range(n)]

mn = min(arr)
mx = max(arr)

# Put elements into buckets
if mn == mx:
    buckets[0] = arr
else:
    for x in arr:
        index = int((x - mn) / (mx - mn) * n)

        if index == n:
            index = n - 1

        buckets[index].append(x)

# Sort individual buckets
for bucket in buckets:
    bucket.sort()

# Combine buckets
result = []
for bucket in buckets:
    result.extend(bucket)


if all(x.is_integer() for x in result):
    print(" ".join(str(int(x)) for x in result))
else:
    print(" ".join(f"{x:.2f}" for x in result))
