
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return True
        flag = 0
        for i in range(n - 1):
                if A[i] > A[i + 1]:
                    if flag == -1:
                        return False
                    flag = 1
                elif A[i] < A[i + 1]:
                    if flag == 1:
                        return False
                    flag = -1
        return True