class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = 1
        zero = 0
        zero_idx = 0

        ans = [0 for _ in range(n)]

        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
                zero_idx = i
            else:
                total *= num

        if zero > 1:
            return ans

        if zero == 1:
            ans[zero_idx] = total

            return ans

        for i in range(n):
            ans[i] = total // nums[i]

        return ans
