class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for col in range(len(matrix[0])):
            r = []
            for row in range(len(matrix)):
                r.append(matrix[row][col])
        
            res.append(r)
        return res