class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        answers = []

        def canPlace(r, c):
            # Check same column
            i = r - 1
            while i >= 0:
                if board[i][c] == "Q":
                    return False
                i -= 1

            # Check upper-left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def queens(row):
            if row == n:
                configuration = ["".join(r) for r in board]
                answers.append(configuration)
                return

            for col in range(n):
                if canPlace(row, col):

                    board[row][col] = "Q"

                    queens(row + 1)

                    board[row][col] = "."

        queens(0)

        return answers
