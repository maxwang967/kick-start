class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pre_sums[i + 1] = self.pre_sums[i] + nums[i]
    def sumRange(self, i: int, j: int) -> int:
        # return sum(self.nums[i: j + 1])
        return self.pre_sums[j + 1] - self.pre_sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)