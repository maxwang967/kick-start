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

    def is_similar(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        if count <= 2:
            return True
        return False
        

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                # equal
                if strs[i] == strs[j]:
                    ds.merge(i, j)
                # if anagram
                if self.is_similar(strs[i], strs[j]):
                    ds.merge(i, j)
                

        return ds.count
