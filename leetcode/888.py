class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)
        # sum_A - x + y = sum_B - y + x
        # x = (sum_A - sum_B + 2 * y) / 2
        memo = set(A)
        for b in B:
            x = (sum_A - sum_B + 2 * b) // 2
            if x in memo:
                return [x, b]