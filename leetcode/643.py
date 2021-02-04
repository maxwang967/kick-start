class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        m_sum = sum(nums[:k])
        result = m_sum / k
        for i, j in zip(nums[:-k], nums[k:]):
            m_sum -= i
            m_sum += j
            mean = m_sum / k
            if mean > result:
                result = mean
        return result