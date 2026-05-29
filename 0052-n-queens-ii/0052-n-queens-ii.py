class Solution:
    def totalNQueens(self, n):

        cols = set()
        diagonal1 = set()
        diagonal2 = set()

        result = [0]

        def backtrack(row):

            if row == n:
                result[0] += 1
                return

            for col in range(n):

                if (
                    col in cols or
                    (row - col) in diagonal1 or
                    (row + col) in diagonal2
                ):
                    continue

                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)

        return result[0]