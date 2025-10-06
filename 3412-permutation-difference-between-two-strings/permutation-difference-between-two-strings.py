class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_index = {}
        t_index = {}
        res = 0

        for i in range(len(s)):
            s_index[s[i]] = i
            t_index[t[i]] = i

        
        for char in s:
            res += abs(s_index[char] - t_index[char])
        
        return res
        