class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg_tree = [0 for _ in range(2*self.n)]
        for i in range(self.n):
            self.seg_tree[self.n+i] = nums[i]
        for i in range(self.n-1, -1, -1):
            self.seg_tree[i] = self.seg_tree[2*i] + self.seg_tree[2*i+1]

    def update(self, index: int, val: int) -> None:
        i = self.n+index
        self.seg_tree[i] = val
        while i > 0:
            l = i
            r = i+1
            
            # if `i` is the right child of its parent
            if i&1 == 1:
                l = i-1
                r = i
                
            self.seg_tree[i//2] = self.seg_tree[l] + self.seg_tree[r]
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        l = self.n+left
        r = self.n+right
        ans = 0
        while l <= r:
            if l&1 == 1:
                ans += self.seg_tree[l]
                l += 1
            l //= 2
            if r&1 == 0:
                ans += self.seg_tree[r]
                r -= 1
            r //= 2
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
