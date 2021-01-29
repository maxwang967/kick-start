class DisjointSet:

    def __init__(self, n):
        self.fa = [x for x in range(n)]

    def get(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.get(self.fa[x])
        return self.fa[x]
    
    def merge(self, x, y):
        if self.get(x) == self.get(y):
            return False
        self.fa[self.get(x)] = self.get(y)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
       m = len(heights)
       n = len(heights[0])
       if m == n == 1:
           return 0
       edges = []
       for i in range(m):
           for j in range(n):
               idx = i * n + j
               if i < m - 1:
                   edges.append([abs(heights[i][j] - heights[i + 1][j]), idx, idx + n])
               if j < n - 1:
                   edges.append([abs(heights[i][j] - heights[i][j + 1]), idx, idx + 1])
       edges.sort()
       ds = DisjointSet(m * n)
       diff = 0
       for e in edges:
           ds.merge(e[1], e[2])
           if ds.get(0) == ds.get(m * n - 1):
               return e[0]
