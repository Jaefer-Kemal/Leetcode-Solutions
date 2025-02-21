# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True

        # Lets first get the middle node then reverse half of it 

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next != None:
            # Lets reverse it iteratively
            prev = slow
            curr = slow.next
            next_node = slow.next.next

            prev.next = None
            curr.next = prev

            while next_node:
                prev = curr
                curr = next_node
                next_node = next_node.next
                curr.next = prev
            
            reversed_second_half = curr

        else:
            # since we only have one node
            reversed_second_half = slow

        # Lets check for palindrome
        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            
            head = head.next
            reversed_second_half = reversed_second_half.next
        
        return True