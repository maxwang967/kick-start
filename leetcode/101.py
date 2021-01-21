# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isMirror(self, nodes: List[TreeNode]):

        if len(nodes) == 1:
            return True
        n = len(nodes)
        for i in range(n // 2):
            if nodes[i] != nodes[n - i - 1]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]
        while q:
            n = len(q)
            l_elements = []
            for _ in range(n):
                node = q.pop(0)
                if node:
                    l_elements.append(node.val)
                else:
                    l_elements.append(None)
                    continue
                q.append(node.left)
                q.append(node.right)
            if not self.isMirror(l_elements):
                return False
        return True