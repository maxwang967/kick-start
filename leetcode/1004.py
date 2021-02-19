class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        N = len(A)
        left = 0
        right = 0
        count_zero = 0
        result = 0
        while left < N and right < N:
            if A[right] == 0:
                count_zero += 1
            while count_zero > K:
                if A[left] == 0:
                    count_zero -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
