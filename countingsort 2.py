def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    result = []
    for num in range(100):
        result.extend([num] * count[num])

    return result


n = int(input())
arr = list(map(int, input().split()))

sorted_arr = countingSort(arr)
print(*sorted_arr)
