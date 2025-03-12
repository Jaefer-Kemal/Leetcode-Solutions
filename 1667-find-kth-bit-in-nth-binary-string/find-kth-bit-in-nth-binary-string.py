class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def generate(n):
            if n == 1:
                return ["0"]
            
            previous = generate(n - 1)

            len_ = len(previous)

            previous.append("1")

            curr = []
            for i in range(len_):
                bit = previous[i]
                if bit == "0":
                    curr.append("1")
                else:
                    curr.append("0")

            return previous + curr[::-1]
        
        res = generate(n)

        return res[k - 1]