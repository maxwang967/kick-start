# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1 recursive
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map_element_index = {
            val: idx for idx, val in enumerate(
                inorder
            )
        }
        def dfs(i: int, j: int) -> TreeNode:
            if i > j:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            idx_inorder = map_element_index[root_val]

            root.right = dfs(idx_inorder + 1, j)
            root.left = dfs(i, idx_inorder - 1)
            return root
        n = len(inorder)
        return dfs(0, n - 1)