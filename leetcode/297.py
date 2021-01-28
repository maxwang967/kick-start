# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        if root is None:
            return result
        q = [root]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                result += str(node.val) + ","
                if node.val == -2000:
                    continue
                if node.left:
                    q.append(node.left)
                else:
                    q.append(TreeNode(-2000))
                if node.right:
                    q.append(node.right)
                else:
                    q.append(TreeNode(-2000))
            # result += ";"
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        level_vals = data.split(",")[:-1]
        # print(level_vals)
        root = TreeNode(level_vals[0])
        q = [root]
        i = 1
        while q and i < len(level_vals):
            cur = q.pop(0)
            if cur is None:
                continue
            # print(i)
            cur.left = TreeNode(int(level_vals[i])) if level_vals[i] != "-2000" else None
            cur.right = TreeNode(int(level_vals[i + 1])) if level_vals[i + 1] != "-2000" else None
            q.append(cur.left)
            q.append(cur.right)
            i += 2
        return root

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))