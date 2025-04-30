class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = s[0]
        ans_sz = 1

        for i in range(n):
            dp[i][i] = True
            j = i + 1
            if j < n and s[i] == s[j]:
                dp[i][j] = True
                ans = s[i:j + 1]
                ans_sz = 2

        for sz in range(3, n + 1):
            for i in range(n - (sz - 1)):
                j = i + (sz - 1)
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = s[i:j + 1]
                    ans_sz = sz

        return ans
