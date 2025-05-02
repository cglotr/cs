class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i1 in range(n1):
            for i2 in range(n2):
                if text1[i1] == text2[i2]:
                    dp[i1 + 1][i2 + 1] = 1 + dp[i1][i2]
                else:
                    dp[i1 + 1][i2 + 1] = max(
                        dp[i1 + 1][i2],
                        dp[i1][i2 + 1]
                    )

        return dp[n1][n2]
