# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        
        def dfs(node):
            nonlocal ans

            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            ans = max(
                ans,
                node.val + l + r
            )

            return max(
                0,
                node.val + l,
                node.val + r
            )

        dfs(root)

        return ans
