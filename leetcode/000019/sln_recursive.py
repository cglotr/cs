# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(prev, node):
            if node is None:
                return 0

            before = remove(node, node.next)

            me = 1 + before
            if me == n:
                prev.next = node.next
            
            return me

        sentinel = ListNode()
        sentinel.next = head

        remove(sentinel, head)

        return sentinel.next
