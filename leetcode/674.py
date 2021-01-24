class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        result = 0
        for i in range(0, n):
            if i > 0 and nums[i] <= nums[i - 1]:
                start = i
                continue
            result = max(result, i - start + 1)
        return result