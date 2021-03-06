class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        result = [0 for _ in range(N)]
        for i in range(2 * N - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i % N]:
                stack.pop()
            result[i % N] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i % N])
        return result
