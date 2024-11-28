class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(s):
            return []
        test = [0]*26
        cnt = [0]*26

        for i in range(k):
            test[ord(p[i])-97] += 1
            cnt[ord(s[i])-97] += 1

        res = []

        if test == cnt:
            res.append(0)
        l = 0

        for r in range(k,len(s)):
            cnt[ord(s[r])-97] += 1
            cnt[ord(s[l])-97] -= 1

            l += 1
            if test == cnt:
                res.append(l)
            
        return res