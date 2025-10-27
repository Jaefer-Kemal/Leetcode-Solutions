# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(None, head)
        prev = dummy
        curr = dummy.next

        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                prev = prev.next
            else:
                element_to_remove = curr.val
                while curr and curr.val == element_to_remove:
                    curr = curr.next

                prev.next = curr
            
        return dummy.next





        