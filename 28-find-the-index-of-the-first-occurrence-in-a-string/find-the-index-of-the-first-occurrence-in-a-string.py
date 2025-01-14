class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1

        for r in range(len(haystack)):
            if haystack[r: r + len(needle)] == needle:
                return r
        
        return -1