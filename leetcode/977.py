class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        negative = None
        for idx, num in enumerate(nums):
            if num < 0:
                negative = idx
            else:
                break
        if negative is None:
            return [x * x for x in nums]
        n = len(nums)
        i = negative
        j = negative + 1
        while i >= 0 or j < n:
            if i < 0:
                result.append(nums[j] ** 2)
                j += 1
            elif j >= n:
                result.append(nums[i] ** 2)
                i -= 1
            elif nums[i] ** 2 < nums[j] ** 2:
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1
        return result

             
