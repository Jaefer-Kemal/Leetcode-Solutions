# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head.next
        prev = head

        while curr:
            prev.val, curr.val = curr.val, prev.val
            if not curr.next or not curr.next.next:
                break
            
            curr = curr.next.next
            prev = prev.next.next
        
        return head

           
        