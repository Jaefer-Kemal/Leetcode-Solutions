class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        longest = s[0]
        max_len = 1
        
        for i in range(n):
            for j in range(i + max_len, n):  # Skip substrings shorter than max_len
                if s[i] == s[j] and is_palindrome(i, j):
                    curr_len = j - i + 1
                    if curr_len > max_len:
                        max_len = curr_len
                        longest = s[i:j + 1]

        return longest
