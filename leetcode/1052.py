class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        original_satisfied_result = 0
        N = len(customers)
        for i in range(N):
            original_satisfied_result += (1 - grumpy[i]) * customers[i]
        window_unsatisfied_value = 0
        for i in range(X):
            window_unsatisfied_value += grumpy[i] * customers[i]
        result = window_unsatisfied_value
        for i in range(X, N):
            if grumpy[i] == 1:
                window_unsatisfied_value += customers[i]
            if grumpy[i - X] == 1:
                window_unsatisfied_value -= customers[i - X]
            result = max(result, window_unsatisfied_value)
        return result + original_satisfied_result