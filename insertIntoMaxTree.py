# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and val < root.val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        else:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root


