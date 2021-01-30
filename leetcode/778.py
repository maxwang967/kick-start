class DisjointSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.count = n

    def get(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.get(self.fa[x])
        return self.fa[x]

    def merge(self, x, y):
        if self.get(x) == self.get(y):
            return False
        self.fa[self.get(x)] = self.get(y)
        self.count -= 1
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ds = DisjointSet(N * N)
        location = {}
        for i in range(N):
            for j in range(N):
                location[grid[i][j]] = i * N + j
                
        t = 0
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        while t <= N * N - 1:
            index = location[t]
            i = index // N
            j = index % N
            for d in directions:
                i1 = i + d[0]
                j1 = j + d[1]
                if i1 >= 0 and i1 < N and j1 >= 0 and j1 < N:
                    if grid[i1][j1] <= t:
                        ds.merge(
                            index, i1 * N + j1
                        )

            if ds.get(0) == ds.get(N * N - 1):
                return t
            t += 1
        return 0
                
