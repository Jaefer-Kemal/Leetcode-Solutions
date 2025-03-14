class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.prefix_sum = [[0] * (self.cols + 1) for row in range(self.rows + 1)]

        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.prefix_sum[row][col] = self.prefix_sum[row - 1][col] + self.prefix_sum[row][col - 1] - self.prefix_sum[row - 1][col - 1] + matrix[row - 1][col - 1]
        print(self.prefix_sum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        submatrix_sum = self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row2 + 1][col1] - self.prefix_sum[row1][col2 + 1] + self.prefix_sum[row1][col1]

        return submatrix_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)