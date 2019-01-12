# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []

        def generate(l, r):
            res = []
            for i in range(l, r + 1):
                for ll in generate(l, i - 1):
                    for rr in generate(i + 1, r):
                        root = TreeNode(i)
                        root.left = ll
                        root.right = rr
                        res += root,
            return res or [None]

        return generate(1, n)


    def generateTrees2(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        from collections import defaultdict
        lookup = defaultdict(list)

        def helper(start, end):
            if start > end:
                return [None]
            if (start, end) in lookup:
                return lookup[(start, end)]

            for val in range(start, end + 1):
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left, root.right = left, right
                        lookup[(start, end)].append(root)
            return lookup[(start, end)]

        return helper(1, n)

