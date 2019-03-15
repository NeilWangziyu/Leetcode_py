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
        if not root:
            return "n"
        s = ""
        stack = [root]
        while (stack):
            root = stack.pop(0)
            if root:
                s += str(root.val)
                stack.append(root.left)
                stack.append(root.right)
            else:
                s += 'n'
            s += ' '
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        tree = data.split()

        if tree[0] == 'n':
            return None

        queue = []
        root = TreeNode(int(tree[0]))
        queue.append(root)
        i = 1
        while (queue):
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != 'n' else None
            cur.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != 'n' else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))