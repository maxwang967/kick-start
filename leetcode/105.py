# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        map_element_idx = {
            val: idx for idx, val in enumerate(inorder)
        }

        def dfs(i: int, j: int) -> TreeNode:
            if i > j:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            idx_inorder = map_element_idx[root_val]
            root.left = dfs(i, idx_inorder - 1)
            root.right = dfs(idx_inorder + 1, j)
            return root

        return dfs(0 , len(preorder) - 1)