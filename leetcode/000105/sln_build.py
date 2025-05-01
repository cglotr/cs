# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_pre = 0
        n = len(inorder)

        def build(l, r):
            if l > r:
                return None
            nonlocal idx_pre

            parent = TreeNode()
            parent.val = preorder[idx_pre]
            idx_pre += 1

            idx = n

            for i in range(l, r + 1):
                if inorder[i] == parent.val:
                    idx = i
                    break

            parent.left = build(l, idx - 1)
            parent.right = build(idx + 1, r)

            return parent

        return build(0, n - 1)
