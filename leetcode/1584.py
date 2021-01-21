class DisjointSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def get(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.get(self.fa[x])
        return self.fa[x]

    def merge(self, x, y):
        if self.get(x) == self.get(y):
            return False
        self.fa[self.get(x)] = self.get(y)
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        result = 0
        edges = []
        n = len(points)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(i + 1, n):
                edges.append(
                    (dist(i, j), i, j)
                )
        edges.sort()
        count = 0
        for d, i, j in edges:
            if ds.merge(i, j):
                result += d
                count += 1
            if count == n:
                break
        return result