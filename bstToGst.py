# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def all_add(self, r, val):
        if not r:
            return
        r.left = self.all_add(r.left, val)
        r.right = self.all_add(r.right, val)
        r.val = r.val + val
        return r

    def sum_all(self, r):
        if not r:
            return 0
        else:
            return r.val + self.sum_all(r.left) + self.sum_all(r.right)

    def bstToGst(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return root

        root.val = root.val + self.sum_all(root.right)

        if root.right:
            root.right = self.bstToGst(root.right)

        if root.left:
            root.left = self.bstToGst(root.left)
        root.left = self.all_add(root.left, root.val)
        return root


class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sums = 0
        self.inOrder(root)
        return root

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.right)
        self.sums += root.val
        root.val = self.sums
        self.inOrder(root.left)


s = Solution()
print(s.bstToGst())