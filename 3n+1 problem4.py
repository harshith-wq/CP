def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count


i, j = map(int, input().split())

original_i, original_j = i, j

if i > j:
    i, j = j, i

max_cycle = 0

for num in range(i, j + 1):
    max_cycle = max(max_cycle, cycle_length(num))

print(original_i, original_j, max_cycle)
