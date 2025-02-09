class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * n
        res = []
        for shift in shifts:
            direction = 1 if shift[2] == 1 else -1
            l = shift[0]
            r = shift[1] + 1
            prefix_sum[l] += direction
            if r != n:
                prefix_sum[r] -= direction

        # res.append(chr((ord(s[0]) + prefix_sum[0] - ord("a")) % 26 + ord("a")))
        shift = 0
        for r in range(n):
            shift += prefix_sum[r]
            res.append(chr((ord(s[r]) + shift - ord("a")) % 26 + ord("a")))

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
                            
        