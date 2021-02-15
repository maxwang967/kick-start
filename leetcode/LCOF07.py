# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 1 recursive
        n = len(preorder)
        if n == 0:
            return None
        def build(i_preorder, j_preorder, i_inorder, j_inorder):
            root_val = preorder[i_preorder]
            root = TreeNode(root_val)
            root_index_inorder = inorder.index(root_val)
            if i_preorder == j_preorder:
                return root
            left_length = root_index_inorder - i_inorder
            if left_length > 0:
                root.left = build(i_preorder + 1, i_preorder + left_length, i_inorder, root_index_inorder - 1)
            if left_length < j_preorder - i_preorder:
                root.right = build(i_preorder + left_length + 1, j_preorder, root_index_inorder + 1, j_inorder)
            return root
        
        return build(0, n - 1, 0, n - 1)