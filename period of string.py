def smallest_period(s):
    n = len(s)
    lps = [0] * n

    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]

        if s[i] == s[j]:
            j += 1
            lps[i] = j

    period = n - lps[-1]

    # The period must divide the whole string
    if n % period == 0:
        return period

    return n


s = input().strip()
print(smallest_period(s))

