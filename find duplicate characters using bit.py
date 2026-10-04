s = input().strip()

seen = 0
duplicates = 0
result = []

for ch in s:
    bit = ord(ch) - ord('a')
    if seen & (1 << bit):
        if not (duplicates & (1 << bit)):
            result.append(ch)
            duplicates |= (1 << bit)
    else:
        seen |= (1 << bit)

if result:
    print(*result)
else:
    print("No duplicates")
