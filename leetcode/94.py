# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 1 iteration
        # result = []
        # stack = []
        # current = root
        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     node = stack.pop()
        #     result.append(node.val)
        #     current = node.right
        # return result
        # 2 morris
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
                    cur = cur.left
                else:
                    result.append(m_right.right.val)
                    m_right.right = None
                    cur = cur.right
            else:
                result.append(cur.val)
                cur = cur.right
        return result