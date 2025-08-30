class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    box = (row//3)*3 + col//3
                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[box]:
                        return False
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    boxes[box].append(board[row][col])
        return True