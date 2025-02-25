# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def debug(self, head):
        curr = head
        while curr:
            print(curr.val, end = "->")
            curr = curr.next
        print(None)
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Lets find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Let reverse the second half of the node

        curr = slow

        if slow.next:
            next_node = slow.next
            remainder = slow.next.next
            next_node.next = curr

        else:
            remainder = None
            next_node = slow

        curr.next = None

        while remainder:
            curr = next_node
            next_node = remainder
            remainder = remainder.next

            next_node.next = curr
        
        twin_sum = 0

        first_head = head
        # reversed middle part of the linkedlist
        second_head = next_node

        # self.debug(first_head)
        # self.debug(next_node)

        while first_head and second_head:
            twin_sum = max(first_head.val + second_head.val, twin_sum)

            first_head = first_head.next
            second_head = second_head.next

        return twin_sum