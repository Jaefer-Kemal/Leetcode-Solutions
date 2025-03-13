# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        # To find the length of the linked list
        while curr:
            length += 1
            curr = curr.next

        curr = head
        # To store the reversed k-groups
        store = []
        # We need to make sure that we can have a group that can be reversed
        while length >= k:
            length -= k
            prev = None

            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            store.append(prev)
        
        dummy = ListNode(-1)
        helper = dummy
        for node in store:
            helper.next = node
            # Reach the end of the node so that we can join it with the other reversed group
            while helper and helper.next:
                helper = helper.next

        # Join the nodes that are not reversed
        helper.next = curr

        return dummy.next