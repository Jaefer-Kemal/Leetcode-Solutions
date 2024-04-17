class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset=set()
        n=len(s)
        l=0
        r=0
        maximum=0
        while r<n:
            if s[r] not in hset:
                hset.add(s[r])
                r+=1
            else:
                if s[l] in hset:
                    hset.remove(s[l])
                    l+=1
            maximum=max(len(hset),maximum)
    
        return maximum
        