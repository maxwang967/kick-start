# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 1 recursive
        # result = []
        # def traversal(node: TreeNode):
        #     if node is None:
        #         return
        #     result.append(node.val)
        #     traversal(node.left)
        #     traversal(node.right)

        # traversal(root)
        # return result

        # 2 iteration
        # stack = []
        # result = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         result.append(node.val)
        #         if node.right:
        #             stack.append(node.right)
        #         if node.left:
        #             stack.append(node.left)
        # return result
        # 3 template iteration
        # result = []
        # current = root
        # stack = []
        # while current or stack:
        #     while current:
        #         result.append(current.val)
        #         stack.append(current)
        #         current = current.left
        #     node = stack.pop()
        #     current = node.right
        # return result
        # 4 morris
        if not root:
            return []
        result = []
        cur = root
        m_right = None

        while cur:
            m_right = cur.left
            if m_right:
                while m_right.right and m_right.right != cur:
                    m_right = m_right.right
                if not m_right.right:
                    m_right.right = cur
                    result.append(cur.val)
                    cur = cur.left
                else:
                    m_right.right = None
                    cur = cur.right
            else:
                result.append(cur.val)
                cur = cur.right

        return result