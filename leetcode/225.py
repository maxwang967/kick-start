class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = collections.deque()
        self.queue_2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = len(self.queue_1)
        if n == 0:
            return None
        while n > 1:
            self.queue_2.append(self.queue_1.popleft())
            n -= 1
        data = self.queue_1.popleft()
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return data
        


    def top(self) -> int:
        """
        Get the top element.
        """
        n = len(self.queue_1)
        return self.queue_1[n - 1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue_1) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()