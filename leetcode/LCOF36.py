"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.cur = node
            if self.pre is None:
                self.head = self.cur
            else:
                self.pre.right = self.cur
                self.cur.left = self.pre
            self.pre = self.cur
            dfs(node.right)
        
        if root is None:
            return None
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
