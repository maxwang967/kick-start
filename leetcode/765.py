class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        result = 0
        for i in range(0, n - 1, 2):
            if row[i] ^ 1 == row[i + 1]:
                continue
            for j in range(i + 1, n):
                if row[i] ^ 1 == row[j]:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    result += 1
        return result
            