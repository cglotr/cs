class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        boundry = 0

        for i in range(n):
            if i <= boundry:
                boundry = max(boundry, i + nums[i])

        return (n - 1) <= boundry
