N = int(input())

count = 0

while N > 0:
    N = N & (N - 1)
    count += 1

print(count)
