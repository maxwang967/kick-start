class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        result = []
        path = []
        nums.sort()
        self.dfs(nums, 0, path, result)
        return result


    def dfs(self, nums, index, path, result):
        result.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()
        