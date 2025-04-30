# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = collections.defaultdict(list)

        def dfs(node, d):
            if node is None:
                return
            lvls[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)

        ans = []

        for k in sorted(lvls.keys()):
            ans.append(lvls[k])

        return ans
