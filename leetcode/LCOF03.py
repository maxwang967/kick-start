class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 1 hashmap 
        # Space Complexity: O(n)
        # if nums is None or len(nums) == 0:
        #     return False
        # memo = {}
        # for num in nums:
        #     if memo.get(num) is not None:
        #         return num
        #     else:
        #         memo[num] = 1
        # 2 in-place
        # Space Complexity: O(1)
        if nums is None or len(nums) == 0:
            return False
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
        return -1
