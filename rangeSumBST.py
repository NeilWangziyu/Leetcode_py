# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    rs = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def search(root):
            if not root: return
            if root.val >= L and root.val <= R:
                self.rs += root.val
            search(root.left)
            search(root.right)

        self.rs = 0
        search(root)

        return self.rs