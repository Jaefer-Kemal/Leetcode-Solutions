class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for col in range(len(matrix[0])):
            part=[]
            for row in range(len(matrix)):
                part.append(matrix[row][col])
            res.append(part)
        return res

