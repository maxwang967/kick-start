class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 1 O(n^2)
        # n = len(nums)
        # if n < 2:
        #     return 0
        # m_sum = 0
        # result = 0
        # for i in range(n - 1):
        #     m_sum = -1 if nums[i] == 0 else 1
        #     for j in range(i + 1, n):
        #         m_sum += -1 if nums[j] == 0 else 1
        #         if m_sum == 0:
        #             result = max(result, j - i + 1)
        # return result
        # 2 partial sum
        n = len(nums)
        if n < 2:
            return 0
        memo = {
            0: -1
        }
        pre_sum = 0
        result = 0
        for i in range(n):
            if nums[i] == 0:
                pre_sum += -1
            else:
                pre_sum += 1
            if memo.get(pre_sum) is not None:
                result = max (result, i - memo.get(pre_sum))
            else:
                memo[pre_sum] = i
        return result
