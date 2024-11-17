from collections import deque
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        merge = ""
        while l < len(word1) and r < len(word2):
            if word1[l:] >= word2[r:]:
                merge += word1[l]
                l += 1
            else:
                merge += word2[r]
                r += 1
            
        if l == len(word1):
            merge += word2[r:]
        else:
            merge += word1[l:]
        
        return merge