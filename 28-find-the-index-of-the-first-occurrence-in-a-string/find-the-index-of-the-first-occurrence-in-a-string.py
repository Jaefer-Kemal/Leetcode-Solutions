class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1

        for r in range(len(haystack)):
            if haystack[r: r + len(needle)] == needle:
                return r
        
        return -1
            




        '''First Solution'''
        # l, r = 0, 0
        # if len(haystack) < len(needle):
        #     return -1
        # while l < len(haystack):
        #     i = l
        #     while l < len(haystack) and r < len(needle) and haystack[l] == needle[r]:
        #         l += 1
        #         r += 1
        #     if r ==len(needle):
        #         return i
            
        #     l = i + 1
            
        #     r = 0
        # return -1
            