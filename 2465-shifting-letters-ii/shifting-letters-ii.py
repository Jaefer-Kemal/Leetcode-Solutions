class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * n
        res = [] * n
        for shift in shifts:
            direction = 1 if shift[2] == 1 else -1
            l = shift[0]
            r = shift[1] + 1
            prefix_sum[l] += direction
            if r != n:
                prefix_sum[r] -= direction

        res.append(chr((ord(s[0]) + prefix_sum[0] - ord("a")) % 26 + ord("a")))

        for r in range(1,n):
            prefix_sum[r] = prefix_sum[r - 1] + prefix_sum[r]
            res.append(chr((ord(s[r]) + prefix_sum[r] - ord("a")) % 26 + ord("a")))

        return "".join(res)





        # res =  ""
        # cnt = defaultdict(int)

        # for shift in shifts:
        #     direction = 1 if shift[2] == 1 else -1
        #     if shift[0] == shift[1]:
        #         cnt[shift[0]] += direction
        #     else:
        #         for i in range(shift[0],shift[1] + 1):
        #             cnt[i] += direction
                
        
        # for  idx, char in enumerate(s):
        #     res += chr((ord(char) + cnt[idx] - ord("a")) % 26 + ord("a"))
        
        # return res
                            
        