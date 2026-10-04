n = int(input().strip())
words = [word.strip() for word in input().split(',')]
pattern = input().strip()
def get_abb(word):
    return ''.join(ch for ch in word if ch.isupper())
def matches_pattern(abbr, pattern):
    j = 0
    for ch in abbr:
        if j < len(pattern) and ch == pattern[j]:
            j += 1
    return j == len(pattern)
result = []
for word in words:
    abbr= get_abb(word)

    if matches_pattern(abbr, pattern):
        result.append((abbr, word))
result.sort(key=lambda x: (x[0], x[1]))
if not result:
    print("No match found")
else:
    for abbr, word in result:
        print(word)
