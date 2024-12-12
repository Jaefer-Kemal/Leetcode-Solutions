class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        flag = True
        for r in range(0,len(s),k):
            if flag:
                res.append(s[r:r+k][::-1])
            else:
                res.append(s[r:r+k])
            flag = not flag 
        return "".join(res)

        