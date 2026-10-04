n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) > len(b):
    a, b = b, a

x, y = len(a), len(b)
low, high = 0, x

while low <= high:
    cut_a = (low + high) // 2
    cut_b = (x + y + 1) // 2 - cut_a

    left_a = float('-inf') if cut_a == 0 else a[cut_a - 1]
    right_a = float('inf') if cut_a == x else a[cut_a]

    left_b = float('-inf') if cut_b == 0 else b[cut_b - 1]
    right_b = float('inf') if cut_b == y else b[cut_b]

    if left_a <= right_b and left_b <= right_a:
        if (x + y) % 2 == 1:
            median = max(left_a, left_b)
            print(f"{median:.1f}")
        else:
            median = (max(left_a, left_b) + min(right_a, right_b)) / 2
            print(f"{median:.1f}")
        break

    elif left_a > right_b:
        high = cut_a - 1
    else:
        low = cut_a + 1
