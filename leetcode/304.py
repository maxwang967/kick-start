class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            M = 0
            N = 0
        else:
            M = len(matrix)
            N = len(matrix[0])
        self.pre_sum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.pre_sum[i + 1][j + 1] = self.pre_sum[i + 1][j] + self.pre_sum[i][j + 1] - self.pre_sum[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)