def find_triplets(arr, x):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicate first elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == x:
                result.append((arr[i], arr[left], arr[right]))

                # Skip duplicate values
                left_val = arr[left]
                right_val = arr[right]

                while left < right and arr[left] == left_val:
                    left += 1

                while left < right and arr[right] == right_val:
                    right -= 1

            elif total < x:
                left += 1
            else:
                right -= 1

    return result


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

triplets = find_triplets(arr, x)

if triplets:
    for a, b, c in triplets:
        print(a, b, c)
else:
    print("No Triplet Found")
