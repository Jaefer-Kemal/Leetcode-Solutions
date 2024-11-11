from collections import deque
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        min_ = len(strs[0])
        for n in strs:
            if n == "":
                return ""
            if min_ >= len(n):
                min_ = len(n)
                value = n

        c = strs[0][0]
        
        c = list(value)
        flag = False
        for i in range(min_):
            for j in range(len(strs)):
                if c[i] != strs[j][i]:
                    flag = True
                    
            if flag:
                break
            l += 1
        if l == 0:
            return ""
        return "".join(c[:l])

                



        



        