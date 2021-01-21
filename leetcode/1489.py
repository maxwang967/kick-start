class DisjointSet:
    def __init__(self, n):
        self.fa = [x for x in range(n)]
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

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        ds = DisjointSet(n)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])
        val = 0
        for i in range(m):
            if ds.merge(edges[i][0], edges[i][1]):
                val += edges[i][2]
        answer = [[], []]
        for i in range(m):
            v = 0
            ds = DisjointSet(n)
            for j in range(m):
                if i != j and ds.merge(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if ds.count != 1 or (ds.count == 1 and v > val):
                answer[0].append(edges[i][3])
                continue
            ds = DisjointSet(n)
            ds.merge(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and ds.merge(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == val:
                answer[1].append(edges[i][3])
        return answer
