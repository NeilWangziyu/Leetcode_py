# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def check(root, value):
            if not root:
                return
            if value == root.val:
                self.count += 1
            check(root.left, value - root.val)
            check(root.right, value - root.val)

        if not root:
            return 0
        check(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.count



