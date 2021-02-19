class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return -1
        lo = 0
        hi = N - 1
        # rotate 0 numbers, numbers is a sorted array
        mid = 0
        while nums[lo] >= nums[hi]:
            if hi - lo == 1:
                mid = hi
                break
            mid = (lo + hi) // 2
            if nums[mid] == nums[lo] and nums[mid] == nums[hi]:
                return min(nums[lo: hi + 1])
            if nums[mid] >= nums[lo]:
                lo = mid
            elif nums[mid] <= nums[hi]:
                hi = mid
        
        return nums[mid]