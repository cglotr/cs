# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = None

        def dfs(node):
            nonlocal count
            nonlocal ans
            if node is None:
                return

            dfs(node.left)

            count -= 1
            if count == 0:
                ans = node.val

            dfs(node.right)

        dfs(root)

        return ans
