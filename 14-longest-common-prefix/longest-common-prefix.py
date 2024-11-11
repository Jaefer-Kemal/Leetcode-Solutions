from collections import deque
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        for n in strs:
            if n == "":
                return ""

        c = strs[0][0]
        strs = sorted(strs)
        c = list(strs[0])
        flag = False
        for i in range(len(strs[0])):

            for j in range(len(strs)):
                if c[i] != strs[j][i]:
                    flag = True
                    
            if flag:
                break
            l += 1
        if l == 0:
            return ""
        return "".join(c[:l])

                



        



        