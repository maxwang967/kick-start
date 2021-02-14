class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1 hashmap space: O(n)
        # memo = set(nums)
        # result = []
        # for i in range(1, len(nums) + 1):
        #     if i not in memo:
        #         result.append(i)
        # return result
        # 2 in-place space: O(1)
        result = []
        n = len(nums)
        for num in nums:
            nums[(num - 1) % n] += n
        for i in range(n):
            if nums[i] <= n:
                result.append(i + 1)
        return result