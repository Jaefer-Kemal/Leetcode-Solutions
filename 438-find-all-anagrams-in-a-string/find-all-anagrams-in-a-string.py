class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        test = Counter(p)
        c = Counter(s[:k])
        res = []
        if test == c:
            res.append(0)
        l = 0
        for r in range(k,len(s)):
            
            c[s[l]] -= 1
            c[s[r]] += 1
                
            l += 1
            if test == c:
                res.append(l)
        return res

