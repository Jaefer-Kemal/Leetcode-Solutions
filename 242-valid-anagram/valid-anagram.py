class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s1 = defaultdict(int)
        t1 = defaultdict(int)
        for r in range(n):
            s1[s[r]] += 1
            t1[t[r]] += 1
        
        if s1 == t1:
            return True
        return False
