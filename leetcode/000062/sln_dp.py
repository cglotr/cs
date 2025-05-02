class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                top = dp[r - 1][c]
                lft = dp[r][c - 1]
                dp[r][c] = dp[r][c] + top + lft

        return dp[m][n]
