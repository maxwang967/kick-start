
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        row = 0
        column = m - 1
        while row < n and column >= 0:
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
        return False