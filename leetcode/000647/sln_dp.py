class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = []

        for i in range(n):
            dp[i][i] = True
            res.append(s[i:i + 1])

        for i in range(n - 1):
            j = i + 1
            if s[i] == s[j]:
                dp[i][j] = True
                res.append(s[i:j + 1])

        for sz in range(3, n + 1):
            for i in range(n - (sz - 1)):
                j = i + (sz - 1)
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res.append(s[i:j + 1])

        return len(res)
