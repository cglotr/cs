class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 2)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 2):
            idx = i - 2
            if 1 <= int(s[idx]) <= 26:
                dp[i] = dp[i] + dp[i - 1]
            if idx > 0 and 10 <= int(s[idx - 1:idx + 1]) <= 26:
                dp[i] = dp[i] + dp[i - 2]

        return dp[-1]
