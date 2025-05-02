# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def rec(root, node):
            if not node:
                return root

            root_new = rec(root, node.next)

            if not root_new:
                return None

            if root_new == node or root_new.next == node:
                node.next = None

                return None
            else:
                tmp = root_new.next

                root_new.next = node
                node.next = tmp

                return tmp

        rec(head, head.next)
