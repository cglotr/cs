class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.dp = [0 for _ in range(n + 1)]

        # prefix sum
        for i in range(n):
            self.dp[i + 1] = nums[i] + self.dp[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right + 1] - self.dp[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
