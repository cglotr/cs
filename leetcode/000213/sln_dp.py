class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(A):
            n = len(A)
            dp = [0 for _ in range(n + 2)]

            for i in range(n):
                dp[i + 2] = max(A[i] + dp[i], dp[i + 1])

            return max(dp)

        return max(
            nums[0],
            rob1(nums[:-1]),
            rob1(nums[1:])
        )
