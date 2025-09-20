class Solution:
    def numSplits(self, s: str) -> int:
        left_split = Counter(s[:1])
        right_split = Counter(s[1:])
        res = 0

        if len(left_split) == len(right_split):
            res += 1

        for i in range(1, len(s)):
            left_split[s[i]] += 1
            right_split[s[i]] -= 1

            if (right_split[s[i]]) == 0:
                del right_split[s[i]]
            
            if len(left_split) == len(right_split):
                res += 1
        
        return res