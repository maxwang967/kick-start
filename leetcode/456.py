class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        left_min = [float((1e9)+1)] * N
        for i in range(1, N):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            num_i = left_min[j]
            num_k = float((-1e9)-1)
            while stack and stack[-1] < nums[j]:
                num_k = stack.pop()
            if num_i < num_k:
                return True
            stack.append(nums[j])
        return False