# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # find the length
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        
        k = k % length

        if k == 0:
            return head

        # circular
        curr.next = head

        steps_to_first_node = length - k
        new_curr = head

        for _ in range(steps_to_first_node - 1):
            new_curr = new_curr.next
        
        new_head = new_curr.next
        new_curr.next = None

        return new_head
        