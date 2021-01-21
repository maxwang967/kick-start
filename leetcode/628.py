class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 1 sort
        # nums.sort()
        # print(nums)
        # first = nums[0]
        # second = nums[1]
        # last = nums[-1]
        # last_2 = nums[-2]
        # last_3 = nums[-3]
        # return max(first * second * last, last * last_2  * last_3)
        # 2 scan
        min1, min2 = 1001, 1001
        max1, max2, max3 = -1001, -1001, -1001
        for n in nums:
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n

            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
        return max(min1 * min2 * max1, max1 * max2 * max3)