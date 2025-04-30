class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)

        for num in nums:
            if num not in dp:
                dp[num] = 1

            for prev, count in dp.items():
                if num > prev:
                    dp[num] = max(dp[num], count + 1)

        return max(dp.values())
