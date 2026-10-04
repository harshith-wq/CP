def longest_palindromic_subsequence(A):
    n = len(A)

    if n == 0:
        return 0

    dp = [1] * n

    for i in range(n - 2, -1, -1):
        prev = 0

        for j in range(i + 1, n):
            temp = dp[j]

            if A[i] == A[j]:
                dp[j] = prev + 2
            else:
                dp[j] = max(dp[j], dp[j - 1])

            prev = temp

    return dp[n - 1]


A = input().strip()
print(longest_palindromic_subsequence(A))
