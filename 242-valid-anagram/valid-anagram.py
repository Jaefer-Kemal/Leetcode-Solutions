class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s1 = [0] * 26
        t1 = [0] * 26
        for r in range(n):
            s1[ord(s[r]) - ord("a")] += 1
            t1[ord(t[r]) - ord("a")] += 1
        
        if s1 == t1:
            return True
        return False
