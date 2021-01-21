# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 1 BFS
        # if root is None:
        #     return False
        # q = [root]
        # q_sum = [root.val]
        # while q:
        #     n = len(q)
        #     for i in range(n):
        #         node = q.pop(0)
        #         cur_sum = q_sum.pop(0)

        #         if cur_sum == targetSum and not node.left and not node.right:
        #             return True
        #         if node.left:
        #             q.append(node.left)
        #             q_sum.append(node.left.val + cur_sum)
        #         if node.right:
        #             q.append(node.right)
        #             q_sum.append(node.right.val + cur_sum)
        # return False  
        # 2 DFS
        if root is None:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)