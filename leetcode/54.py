class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        x = 0
        y = 0
        cur_d = 0
        # right, bottom, left, top
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        left = 0
        right = cols - 1
        top = 0
        bottom = rows - 1
        while len(result) < rows * cols:
            result.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                top += 1
            elif cur_d == 1 and x == bottom:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                bottom -= 1
            elif cur_d == 3 and x == top:
                cur_d += 1
                left += 1
            cur_d = cur_d % 4
            x += directions[cur_d][0]
            y += directions[cur_d][1]
        return result
