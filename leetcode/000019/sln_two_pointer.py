# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        lf = dummy
        rg = head

        for _ in range(n):
            rg = rg.next

        while rg is not None:
            lf = lf.next
            rg = rg.next

        lf.next = lf.next.next

        return dummy.next
