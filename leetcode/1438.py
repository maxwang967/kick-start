class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        window = SortedList()
        left = 0
        right = 0
        result = 0
        while right < len(nums):
            window.add(nums[right])
            if window[-1] - window[0] > limit:
                window.remove(nums[left])
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result