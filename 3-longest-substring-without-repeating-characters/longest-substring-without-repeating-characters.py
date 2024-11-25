class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        maximum = 0
        for r in range(len(s)):
            if s[r] not in check:
                check.add(s[r])
            else:
                while s[r] in check:
                    check.remove(s[l])
                    l += 1
                check.add(s[r])

            maximum = max(maximum,len(check))
        return maximum
        