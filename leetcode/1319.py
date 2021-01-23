class DisjointSet:
    def __init__(self, n) -> None:
        self.n = n
        self.fa = [i for i in range(n)]
    
    def get(self, x: int):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.get(self.fa[x])
        return self.fa[x]
    
    def merge(self, x: int, y: int):
        if self.get(x) == self.get(y):
            return False
        self.fa[self.get(x)] = self.get(y)
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        con_length = len(connections)
        if con_length < n - 1:
            return -1
        ds = DisjointSet(n)
        count = 0
        for edge in connections:
            ds.merge(edge[0], edge[1])
        for i in range(n):
            if ds.get(i) == i:
                count += 1
        return count - 1
