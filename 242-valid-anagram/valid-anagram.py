class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s1 = Counter()
        t1 = Counter()
        for r in range(n):
            s1[s[r]] += 1
            t1[t[r]] += 1
        
        if s1 == t1:
            return True
        return False
