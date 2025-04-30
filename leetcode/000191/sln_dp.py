class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 2)]
        
        for i in range(n):
            dp[i + 2] = max(nums[i] + dp[i], dp[i + 1])

        return max(dp)
