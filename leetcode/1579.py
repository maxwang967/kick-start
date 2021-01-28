class DisjointSet:

    def __init__(self, n):
        self.fa = [x for x in range(n)]
        self.count = n
    
    def get(self, x: int):
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DisjointSet(n)
        bob = DisjointSet(n)
        result = 0
        for e in edges:
            e[1] -= 1
            e[2] -= 1
        
        for e in edges:
            if e[0] == 3:
                if not alice.merge(e[1], e[2]):
                    result += 1
                else:
                    bob.merge(e[1], e[2])
        
        for e in edges:
            if e[0] == 1:
                if not alice.merge(e[1], e[2]):
                    result += 1
            elif e[0] == 2:
                if not bob.merge(e[1], e[2]):
                    result += 1
        # impossible case
        if alice.count != 1 or bob.count != 1:
            return -1
        
        return result