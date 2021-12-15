class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        dr = {}
        dc = {}
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    dr[r] = 1
                    dc[c] = 1
        for r in dr:
            for c in range(cols):
                matrix[r][c] = 0
        for c in dc:
            for r in range(rows):
                matrix[r][c] = 0
