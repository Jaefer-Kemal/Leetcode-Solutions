class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        if k > 0:
            for i in range(n):
                sum_ = 0
                for j in range(1, k + 1):
                    index = (i + j) % n
                    sum_ += code[index]
                res[i] = sum_
                
        else:  # k < 0
            for i in range(n):
                sum_ = 0
                for j in range(1, abs(k) + 1):
                    index = (i - j) % n
                    sum_ += code[index]
                res[i] = sum_
                
        return res
