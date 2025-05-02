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
        def rev(node):
            if not node or not node.next:
                return node

            root = rev(node.next)

            node.next.next = node
            node.next = None

            return root

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        lft = head
        rgt = rev(slow)

        while lft:
            lft_tmp = lft.next
            rgt_tmp = rgt.next

            lft.next = rgt
            rgt.next = lft_tmp

            lft = lft_tmp
            rgt = rgt_tmp
