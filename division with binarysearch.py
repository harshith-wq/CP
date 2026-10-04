def divide(x, y):
    if y == 0:
        return "Division by zero"
    negative = (x < 0) != (y < 0)
    x = abs(x)
    y = abs(y)
    low = 0
    high = x

    while low <= high:
        mid = (low + high) // 2

        if y * mid == x:
            result = mid
            break
        elif y * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    else:
        result = high

    if negative:
        result = -result

    return result


x, y = map(int, input().split())
print(divide(x, y))
