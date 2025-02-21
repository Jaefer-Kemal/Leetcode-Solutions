# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        even_nodes = ListNode(-1)
        odd_nodes = ListNode(-1)

        curr = head
        
        head_of_even = even_nodes
        head_of_odd = odd_nodes

        count = 1
        while curr:
            if count % 2 == 0:
                even_nodes.next = curr
                even_nodes = even_nodes.next
            else:
                odd_nodes.next = curr
                odd_nodes = odd_nodes.next
            
            curr = curr.next
            count += 1

        even_nodes.next = None

        odd_nodes.next = head_of_even.next

        return head_of_odd.next
