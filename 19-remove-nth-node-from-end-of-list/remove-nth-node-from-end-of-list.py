# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = 0

        # Checking the length of linkedlist
        while curr:
            length += 1
            curr = curr.next
                        
        position = length 

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr:
            if position == n:
                curr.next = curr.next.next
                break
                
            curr = curr.next
            position -= 1

        return dummy.next