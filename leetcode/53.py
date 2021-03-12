class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # max_sum = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        #     if dp[i] > max_sum:
        #         max_sum = dp[i]
        # return max_sum
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)