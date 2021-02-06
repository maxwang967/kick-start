class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        window = sum(cardPoints[:n - k])
        result = total_sum - window
        for i in range(1, k+1):
            window -= cardPoints[i - 1]
            window += cardPoints[i + n - k - 1]
            result = max(result, total_sum - window)
        return result
            