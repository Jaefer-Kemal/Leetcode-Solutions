# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        curr = curr.next
        while curr:
            if curr and curr.next:

                prev = curr.val
                forw = curr.next.val

                curr.val = forw
                curr.next.val = prev
                curr = curr.next.next
                
            else:
                break

        return dummy.next
        