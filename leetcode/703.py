class Heap:

    def __init__(self, desc=False):
        self.heap = []
        self.desc = desc
    
    @property
    def size(self):
        return len(self.heap)

    def top(self):
        return self.heap[0]
    
    def push(self, x):
        self.heap.append(x)
        self._sift_up(self.size - 1)
    
    def pop(self):
        ans = self.heap[0]
        # print(f"before: {self.heap}")
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        # print(f"after: {self.heap}")
        self._sift_down(0)
        return ans

    
    def _sift_down(self, index):
        while index * 2 + 1 < self.size:
            smallest = index
            if self._smaller(self.heap[index * 2 + 1], self.heap[smallest]):
                smallest = index * 2 + 1
            if index * 2 + 2 < self.size:
                if self._smaller(self.heap[index * 2 + 2], self.heap[smallest]):
                    smallest = index * 2 + 2
            if index == smallest:
                break
            self._swap(index, smallest)
            index = smallest


    def _sift_up(self, index):
        while index:                
            if self._smaller(self.heap[(index - 1) // 2], self.heap[index]):
                break
            self._swap((index - 1) // 2, index)
            index = (index - 1) // 2


    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _smaller(self, x, y):
        return x > y if self.desc else x < y
    
    


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 1 manually
        # self.heap = Heap()
        # for num in nums:
        #     self.heap.push(num)
        #     if self.heap.size > k:
        #         self.heap.pop()
        # 2 lib
        self.heap = nums
        heapq.heapify(self.heap)

        

    def add(self, val: int) -> int:
        # 1 manually
        # self.heap.push(val)
        # # print(f"before: {self.heap.heap}")
        # if self.heap.size > self.k:
        #     self.heap.pop()
        # # print(f"after: {self.heap.heap}")
        # return self.heap.top()
        # 2 lib
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)