class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        result = [[0] * n for _ in range(n)]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        # right, bottom, left, top
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        x = 0
        y = 0
        cur_d = 0
        while count != n * n:
            result[x][y] = count + 1
            count += 1
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