class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for row in range(len(matrix[0])):
            r = []
            for col in range(len(matrix)):
                r.append(matrix[col][row])
        
            res.append(r)
        return res