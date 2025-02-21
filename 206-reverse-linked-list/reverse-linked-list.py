# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        curr = head
        next = head.next
        remainder = next.next
        curr.next = None
        next.next = curr

        while remainder:
            curr = next
            next = remainder
            remainder = remainder.next
            next.next = curr
        
        return next
