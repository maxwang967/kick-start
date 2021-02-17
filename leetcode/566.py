class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n !=  r * c:
            return nums
        result = [[0] * c for _ in range(r)]
        # (i, j) -> i * n + j
        for x in range(m * n):
            result[x // c][x % c] = nums[x // n][x % n]
        return result