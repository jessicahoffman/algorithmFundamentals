class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = [1] * len(matrix)
        col = [1] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:

                    row[r] = 0
                    col[c] = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if row[r] == 0:
                    matrix[r] = [0] * len(matrix[0])
                    break
                elif col[c] == 0:  # and not matrix[r][c] == 0:
                    matrix[r][c] = 0
