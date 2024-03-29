class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = (n - 1) & n
        return count