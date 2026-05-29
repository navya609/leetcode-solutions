class Solution:
    def solveNQueens(self, n):

        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonal1 = set()
        diagonal2 = set()

        def backtrack(row):

            if row == n:
                result.append(
                    ["".join(r) for r in board]
                )
                return

            for col in range(n):

                if (
                    col in cols
                    or (row - col) in diagonal1
                    or (row + col) in diagonal2
                ):
                    continue

                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."

                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)

        return result