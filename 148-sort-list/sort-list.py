# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergedArray(self, left, right):
        merged = ListNode(-1)
        temp = merged
        i = 0
        j = 0
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next

            temp = temp.next
        
        if left:
            temp.next = left
        
        if right:
            temp.next = right
        
        return merged.next

    
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        mid = prev
        mid.next = None

        first = head
        second = slow

        left = self.sortList(first)
        right = self.sortList(second)

        return self.mergedArray(left, right)