class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 1 complex solution 
        # l = len(nums)
        # right = 0
        # k = 1
        # while right < l:
        #     for i in range(0, right):
        #         if nums[i] > nums[i + 1]:
        #             if k > 0:
        #                 k -= 1
        #                 if i + 2 < l and i - 1 >= 0:
        #                     if nums[i] >= nums[i - 1] and nums[i] <= nums[i + 2]:
        #                         nums[i + 1] = nums[i]
        #                     else:
        #                         nums[i] = nums[i + 1]
        #                 else:
        #                     nums[i] = nums[i + 1]
        #             else:
        #                 return False   
        #     right += 1     
        # return True
        # 2 greedy
        k = 0
        l = len(nums)
        for i in range(1, l):
            if k > 1:
                return False
            if nums[i] >= nums[i - 1]:
                continue
            k += 1
            if i - 2 >= 0 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] == nums[i]
        return k <= 1
