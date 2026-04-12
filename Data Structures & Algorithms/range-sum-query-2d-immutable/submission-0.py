class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.prefixMat = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            prefixSum = 0
            for c in range(COLS):
                prefixSum += matrix[r][c]
                above = self.prefixMat[r][c+1]
                self.prefixMat[r+1][c+1] = prefixSum + above

        print(self.prefixMat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1
        # print(self.prefix_matrix)

        result = self.prefixMat[r2][c2] - self.prefixMat[r1-1][c2] - self.prefixMat[r2][c1-1] + self.prefixMat[r1-1][c1-1]

        return result

# param_1 = obj.sumRegion(row1,col1,row2,col2)