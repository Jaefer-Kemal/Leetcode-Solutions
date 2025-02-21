# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head


        smaller_nodes = ListNode(-1)
        greater_nodes = ListNode(-1)
        
        curr = head

        first = smaller_nodes
        end = greater_nodes

        while curr:
            if curr.val < x:
                smaller_nodes.next = curr
                smaller_nodes = smaller_nodes.next
            else:
                greater_nodes.next = curr
                greater_nodes = greater_nodes.next
        

            curr = curr.next

        smaller_nodes.next = end.next
        greater_nodes.next = None

        return first.next


            

        