class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        pw = 0
        while 2**pw < self.n:
            pw += 1
        n = 2**pw
        sz = 2*n - 1
        self.seg_tree = [0 for _ in range(sz)]

        def construct(l, r, pos):
            # segment tree leaf
            if l >= r:
                self.seg_tree[pos] = nums[l]
                return

            m = l + (r - l)//2
            pos_l = 2*pos + 1
            pos_r = 2*pos + 2

            construct(l, m, pos_l)
            construct(m + 1, r, pos_r)

            self.seg_tree[pos] = self.seg_tree[pos_l] + self.seg_tree[pos_r]
            return

        construct(0, self.n - 1, 0)

    def sumRange(self, left: int, right: int) -> int:
        def query(l, r, pos):
            # total overlap
            if l >= left and r <= right:
                return self.seg_tree[pos]

            # no overlap
            if l > right or r < left:
                return 0
            m = l + (r - l)//2

            # partial overlap
            ql = query(l, m, 2*pos + 1)
            qr = query(m + 1, r, 2*pos + 2)

            return ql + qr

        return query(0, self.n - 1, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
