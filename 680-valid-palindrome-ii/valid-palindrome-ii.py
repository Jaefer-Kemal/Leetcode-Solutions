class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        flag1 = True
        flag2 = True
        while left < right:
            if s[left] != s[right]:
                if flag1:
                    l = left
                    r = right
                    right -= 1
                    flag1 = False
                    continue
                elif flag2:
                    right = r
                    left = l + 1
                    flag2 = False
                    continue
                return False
            left += 1
            right -= 1
        return True
        