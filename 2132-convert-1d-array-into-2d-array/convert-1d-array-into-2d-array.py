class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        res = []
        l = 0
        for row in range(m):
            row = []
            for col in range(n):
                row.append(original[l])
                l += 1
            res.append(row)

        return res
                
