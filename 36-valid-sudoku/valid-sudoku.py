class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validate_rows = defaultdict(set)
        validate_cols = defaultdict(set)
        print(board)
        for row in range(9):
            for col in range(9):
                cell = board[row][col]

                if cell != ".":
                    if (cell in validate_rows[row] or cell in validate_cols[col]):
                        print(cell)
                        print(validate_rows[row], row)
                        print(validate_cols[col], col)
                        return False
                
                    validate_rows[row].add(cell)
                    validate_cols[col].add(cell)

        col_range = [[6,9],[3,6],[0,3]]
        row_range = [[6,9],[3,6],[0,3]]

        while row_range:
            row_start, row_end = row_range.pop()
            n = 3
            while n:
                col_start, col_end = col_range[n - 1]
                n -= 1
                validate_grid = set()
                for row in range(row_start, row_end):
                    for col in range(col_start, col_end):
                        cell = board[row][col]

                        if cell != ".":
                            if cell in validate_grid:
                                return False
                            
                            validate_grid.add(cell)
        
        return True

        
        


        