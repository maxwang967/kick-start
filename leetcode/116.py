"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 1 BFS
        # if root is None:
        #     return None
        # q = [root]
        # while q:
        #     n = len(q)
        #     for i in range(n):
        #         node = q.pop(0)
        #         if i + 1 < n:
        #             node.next = q[0]
        #         else:
        #             node.next = None
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return root

        # 2 DFS
        if root is None:
            return None
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root