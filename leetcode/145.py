# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def print_right_edge(root: TreeNode):
            cur = root
            pre = None
            while cur:
                next_node = cur.right
                cur.right = pre
                pre = cur
                cur = next_node

            cur = pre
            while cur:
                result.append(cur.val)
                cur = cur.right

            cur = pre
            pre = None
            while cur:
                next_node = cur.right
                cur.right = pre
                pre = cur
                cur = next_node
        # 1 iteration, not likely to stacktrace
        # result = []
        # stack = []
        # current = root
        # while current or stack:
        #     while current:
        #         result.append(current.val)
        #         stack.append(current)
        #         current = current.right
        #     node = stack.pop()
        #     current = node.left
        # return result[::-1]
        # 2 iteration, stacktrace based
        # result = []
        # stack = []
        # stack.append((0, root))
        # while stack:
        #     flag, node = stack.pop()
        #     if not node:
        #         continue
        #     if flag == 1:
        #         result.append(node.val)
        #     else:
        #         stack.append((1, node))
        #         stack.append((0, node.right))
        #         stack.append((0, node.left))
        # return result
        # 3 morris
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
                    cur = cur.left
                else:
                    m_right.right = None
                    print_right_edge(cur.left)
                    cur = cur.right
            else:
                cur = cur.right
        print_right_edge(root)
        return result