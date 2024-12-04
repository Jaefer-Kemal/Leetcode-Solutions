class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()

        l = 0
        max_len = 0
        for r in range(len(s)):
            char = s[r]
            while char in check and l < r:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            max_len = max(max_len,r - l + 1)
        
        return max_len