# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    # 1 top-bottom
    # def dfs(self, root: TreeNode, depth: int):
    #     if root is None:
    #         return
    #     if root.left is None and root.right is None:
    #         self.result = max(self.result, depth)
    #     self.dfs(root.left, depth + 1)
    #     self.dfs(root.right, depth + 1) 

    # def maxDepth(self, root: TreeNode) -> int:
    #     self.result = 0
    #     depth = 1
    #     self.dfs(root, depth)
    #     return self.result

    # 2 bottom-top
    # def maxDepth(self, root: TreeNode) -> int:

    #     def dfs(root: TreeNode):
    #         if root is None:
    #             return 0
    #         left_depth = dfs(root.left)
    #         right_depth = dfs(root.right)
    #         return max(left_depth, right_depth) + 1

    #     return dfs(root)

    # 3 BFS
        def maxDepth(self, root: TreeNode) -> int:
            if root is None:
                return 0
            q = [root]
            level = 0
            while q:
                n = len(q)
                for i in range(n):
                    node = q.pop(0)
                    if node.left:
                       q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1
            return level
