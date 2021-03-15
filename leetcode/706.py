class MyHashMap(object):

    def __init__(self):
        # self.hashmap = [[-1] * 1000 for _ in range(1001)]
        self.buckets = 1009
        self.hashmap = [[] for _ in range(self.buckets)]
    
    def hash(self, key):
        return key % self.buckets

    def put(self, key, value):
        # row, col = key // 1000, key % 1000
        # self.hashmap[row][col] = value
        hash_key = self.hash(key)
        for item in self.hashmap[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        self.hashmap[hash_key].append([key, value])


    def get(self, key):
        # row, col = key // 1000, key % 1000
        # return self.hashmap[row][col]
        hash_key = self.hash(key)
        for item in self.hashmap[hash_key]:
            if item[0] == key:
                return item[1]
        return -1


    def remove(self, key):
        # row, col = key // 1000, key % 1000
        # self.hashmap[row][col] = -1
        hash_key = self.hash(key)
        for i, item in enumerate(self.hashmap[hash_key]):
            if item[0] == key:
                self.hashmap[hash_key].pop(i)