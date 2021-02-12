class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 1 normal
        # space complexity: O(k^2)
        result = [
            [1 for _ in range(i + 1)] for i in range(rowIndex + 1)
        ]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result[-1]
        # 2 dp
        # space complexity: O(k)
        result = [1 for _ in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            result[0] = 1
            result[i] = 1
            for j in range(i - 1, 0, -1):
                result[j] = result[j] + result[j - 1]
        return result

