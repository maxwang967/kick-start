# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.elements = []
        self.inorder(root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.elements.append(node.val)
        self.inorder(node.right)
        

    def next(self) -> int:
        return self.elements.pop(0)


    def hasNext(self) -> bool:
        return True if self.elements else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()