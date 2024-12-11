class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0 :
            return res
        
        elif k > 0:
            for i in range(len(code)):
                cnt = k
                j = i + 1
                sum_ = 0
                while cnt > 0:
                    index = j % len(code)
                    if index != i:
                        sum_ += code[index]
                        cnt -= 1
                    j += 1
                res[i] = sum_
                        
        else:
            for i in range(len(code)):
                cnt = k
                j = i - 1
                sum_ = 0
                for j in range(1, abs(k) + 1):
                    index = (i - j) % len(code)
                    sum_ += code[index]
    
                res[i] = sum_
        return res

                    


        