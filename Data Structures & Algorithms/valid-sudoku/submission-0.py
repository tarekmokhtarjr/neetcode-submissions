class Solution:
    def validPoint(self, board: List[List[str]], row: int, column: int) -> bool:
        if row > 5:
            row_init = 6
        elif (row <= 5 and row > 2):
            row_init = 3
        else:
            row_init = 0

        if column > 5:
            column_init = 6
        elif (column <= 5 and column > 2):
            column_init = 3
        else:
            column_init = 0
        for r in range(row_init, row_init+3):
            for c in range(column_init, column_init+3):
                if r != row and c != column:
                    if board[r][c] == board[row][column]:
                        return False
        for r in range(0, 9):
            if r != row:
                if board[r][column] == board[row][column]:
                    return False
        for c in range(0, 9):
            if c != column:
                if board[row][c] == board[row][column]:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] != ".":
                    if not self.validPoint(board, r, c):
                        return False
        return True
        