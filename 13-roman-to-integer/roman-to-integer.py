class Solution:
    def romanToInt(self, s: str) -> int:
        memo = {"I":1, "V":5, "X":10, "L": 50,"C":100,"D":500,"M":1000}
        l = 0
        sum_ = 0
        while l < len(s):
            if l == len(s) - 1:
                sum_ += memo[s[l]]
            elif s[l] in "I":
                if s[l+1] == "V" or s[l+1] == "X":
                    sum_ += (memo[s[l+1]] - 1)
                    l += 1
                else:
                    sum_ += 1
            elif s[l] == "X":
                if s[l+1] == "L" or s[l+1] == "C":
                    sum_ += (memo[s[l+1]] - 10)
                    l += 1
                else:
                    sum_ += 10
            elif s[l] == "C":
                if s[l+1] == "D" or s[l+1] == "M":
                    sum_ += (memo[s[l+1]] - 100)
                    l += 1
                else:
                    sum_ += 100
            else:
                sum_ += memo[s[l]]
            l += 1
        return sum_
           