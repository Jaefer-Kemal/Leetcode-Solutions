class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = 0
        cnt = defaultdict(int)
        l = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            while len(cnt) == 3:
                length += len(s) - r
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
        return length

        