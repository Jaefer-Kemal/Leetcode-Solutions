class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        max_len = 0
        for i in range(len(s)):
            for j in range(i + max_len,len(s)):
                flag = True
                left = i
                right = j
                while left <= right:
                    if s[left] != s[right]:
                        flag = False
                        break
                    left += 1
                    right -= 1
                if flag and j - i + 1 > max_len:
                    max_len = j - i + 1
                    longest = s[i:j + 1]
        return longest
            
                