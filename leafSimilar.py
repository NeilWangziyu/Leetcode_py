# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res = []

        def pre_order(root):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            else:
                pre_order(root.left)
                pre_order(root.right)

        pre_order(root1)
        res1 = res
        res = []
        pre_order(root2)
        print(res1, res)
        if res1 == res:
            return True
        else:
            return False