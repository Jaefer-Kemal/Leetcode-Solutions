class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        flag = True
        for r in range(0,len(s),k):
            if flag:
                res += s[r:r+k][::-1]
                flag = False
            else:
                res += s[r:r+k]
                flag = True
        return res

        