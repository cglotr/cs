class NumArray:

    def __init__(self, nums: List[int]):
        def construct(l, r):
            node = SegTreeNode()
            node.lo = l
            node.hi = r
            if l >= r:
                node.vl = nums[l]
                return node
            md = l+(r-l)//2

            node.cl = construct(l, md)
            node.cr = construct(md + 1, r)

            node.vl = node.cl.vl + node.cr.vl
            return node

        self.root = construct(0, len(nums) - 1)

    def sumRange(self, left: int, right: int) -> int:
        def query(node):
            if node.lo >= left and node.hi <= right:
                return node.vl
            if node.lo > right or node.hi < left:
                return 0

            return query(node.cl) + query(node.cr)

        return query(self.root)


class SegTreeNode:
    
    def __init__(self):
        self.vl = 0
        self.lo = 0
        self.hi = 0
        self.cl = None
        self.cr = None 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
