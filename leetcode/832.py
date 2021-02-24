class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        for i in range(N):
            for j in range((N + 1) // 2):
                A[i][j], A[i][N - 1 - j] = 1 - A[i][N - 1 - j], 1 - A[i][j]
        return A