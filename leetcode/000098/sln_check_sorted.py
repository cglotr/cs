# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return []

            l = dfs(node.left)
            r = dfs(node.right)

            return l + [node.val] + r

        ans = dfs(root)

        return ans == sorted(list(set(ans)))
