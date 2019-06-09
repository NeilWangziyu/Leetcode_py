# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
    #     def sufficientSubset_core(root: TreeNode, limit: int):
    #         if not root:
    #             return None
    #         if root.left:
    #             root.left = self.sufficientSubset(root.left, limit = limit - root.val)
    #         if root.right:
    #             root.right = self.sufficientSubset(root.right, limit=limit - root.val)
    #         if not root.left and not root.right:
    #             if root.val < limit:
    #                 return None
    #         return root
    #     root = sufficientSubset_core(root,limit)
    #     return root

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        """
        报错
        """
        if not root:
            return None
        if root.left:
            root.left = self.sufficientSubset(root.left, limit = limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit = limit - root.val)
        if not root.left and not root.right:
            if root.val < limit:
                return None
        return root

    def sufficientSubset2(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """

        def dfs(node, sum_):
            if not node:
                return sum_, sum_ >= limit
            sum_ += node.val
            left, lf = dfs(node.left, sum_)
            right, rf = dfs(node.right, sum_)
            if not lf:
                node.left = None
            if not rf:
                node.right = None
            path_sum = max(left, right)
            return path_sum, path_sum >= limit

        sum_, flag = dfs(root, 0)
        if not flag:
            return None
        return root
