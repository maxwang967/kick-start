class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(T))]
        for i in range(len(T) - 1, -1, -1):
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            result[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)
        return result