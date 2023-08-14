class NumArray:

    def __init__(self, nums: List[int]):
        self.inf = 3*10**4
        self.seg_tree = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        self._update(index, val, 0, self.inf-1, 1)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(left, right, 0, self.inf-1, 1)
        
    def _sum(self, l, r, seg_l, seg_r, pos):
        if seg_l > r or seg_r < l:
            return 0
        if seg_l >= l and seg_r <= r:
            return self.seg_tree[pos]
        m = (seg_r - seg_l)//2 + seg_l
        l_sum = self._sum(l, r, seg_l, m, 2*pos)
        r_sum = self._sum(l, r, m+1, seg_r, 2*pos+1)
        return self.lazy[pos] + l_sum + r_sum
        
    def _update(self, i, v, seg_l, seg_r, pos):
        if seg_l > i or seg_r < i:
            return
        if seg_l >= i and seg_r <= i:
            self.lazy[pos] = v
        else:
            m = (seg_r - seg_l)//2 + seg_l
            self._update(i, v, seg_l, m, 2*pos)
            self._update(i, v, m+1, seg_r, 2*pos+1)
        self.seg_tree[pos] = self.lazy[pos] + self.seg_tree[2*pos] + self.seg_tree[2*pos+1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
