class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        memo = {
            0: -1
        }
        m_sum = 0
        result = 0
        for i in range(len(nums)):
            m_sum += nums[i]
            if memo.get(m_sum - k) is not None:
                end_index = memo[m_sum - k]
                result = max(result, i - end_index)
            if memo.get(m_sum) is None:
                memo[m_sum] = i
        return result