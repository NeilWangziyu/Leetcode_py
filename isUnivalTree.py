# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def check_same(root_t, val):
            if not root_t:
                return True
            if root_t.val != val:
                return False
            if check_same(root_t.left, val) and check_same(root_t.right, val):
                return True
            else:
                return False

        return check_same(root, root.val)