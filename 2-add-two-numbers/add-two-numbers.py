# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2

        l3 = ListNode(-1)
        curr_3 = l3
        
        carry = 0
        while curr_1 or curr_2 or carry:
            if curr_1:
                l1_digit = curr_1.val
            else:
                l1_digit = 0
            if curr_2:
                l2_digit = curr_2.val
            else:
                l2_digit = 0

            add = l1_digit + l2_digit + carry

            if add > 9:
                carry = 1
                add = add % 10
            else:
                carry = 0
            
            new_node = ListNode(add)
            curr_3.next = new_node
            curr_3 = curr_3.next

            if curr_1:
                curr_1 = curr_1.next

            if curr_2:
                curr_2 = curr_2.next

        return l3.next

