class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # since we can delete atmost one character 
                # we are going to check if deleting the recent character in the left index
                # or recent character in the right index will suffice
                return helper_palindrome(left + 1,right) or helper_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True

            
        