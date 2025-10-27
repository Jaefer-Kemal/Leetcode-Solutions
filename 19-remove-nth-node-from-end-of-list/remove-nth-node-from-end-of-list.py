# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        # Length of list
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        
        dummy = ListNode(-1, head)
        curr = dummy
        jump = length - n
        i = 0
        while curr:
            if i == jump:
                curr.next = curr.next.next
            
            i += 1
            curr = curr.next
        
        return dummy.next
         