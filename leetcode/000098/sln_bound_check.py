# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, l, r):
            if node is None:
                return True

            if node.val < l or node.val > r:
                return False

            cl = check(node.left, l, node.val - 1)
            cr = check(node.right, node.val + 1, r)

            return cl and cr

        return check(root, -math.inf, math.inf)
