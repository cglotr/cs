class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_zero = False
        col_zero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    if r == 0:
                        row_zero = True
                    if c == 0:
                        col_zero = True

        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(n):
                    matrix[r][c] = 0

        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(m):
                    matrix[r][c] = 0

        if row_zero:
            for c in range(n):
                matrix[0][c] = 0

        if col_zero:
            for r in range(m):
                matrix[r][0] = 0
