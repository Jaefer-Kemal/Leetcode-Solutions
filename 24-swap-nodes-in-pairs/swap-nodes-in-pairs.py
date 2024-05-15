# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        curr = head
        while head:
            if head and head.next:

                prev = head.val
                forw = head.next.val

                head.val = forw
                head.next.val = prev
                head = head.next.next
            else:
                break
                
        return curr
        