class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for column in range(row,len(matrix[0])):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
       
        for row in range(len(matrix)):
            for col in range(len(matrix[0])//2):
                matrix[row][col], matrix[row][-(col + 1)] = matrix[row][-(col + 1)], matrix[row][col]
                
                
                    
        