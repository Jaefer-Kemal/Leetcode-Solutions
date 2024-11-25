class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        maximum = 0
        for r in range(len(s)):
            if s[r] not in check:
                check.add(s[r])
            else:
                while s[r] in check and s[l] in check and l < len(s) and l < r:
                    check.remove(s[l])
                    l += 1
                check.add(s[r])

            maximum = max(maximum,len(check))
        return maximum
        