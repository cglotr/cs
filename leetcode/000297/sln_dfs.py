# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def dfs(node):
            if not node:
                ans.append('n')
                return

            ans.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        idx = 0

        def dfs():
            nonlocal idx

            v = arr[idx]
            idx += 1

            if v == 'n':
                return None

            node = TreeNode()
            node.val = int(v)

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
