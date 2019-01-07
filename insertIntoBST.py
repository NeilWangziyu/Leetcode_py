# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def insert(check, val):
            if not check:
                return TreeNode(val)
            else:
                if val > check.val:
                    check.right = insert(check.right, val)
                else:
                    check.left = insert(check.left, val)
            return check

        if not root:
            return TreeNode(val)

        root = insert(root, val)
        return root

