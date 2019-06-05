# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    resMax = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def longestUnvpath_core(r):
            if not r:
                return 0
            temRes = 0
            leftMaxVal = longestUnvpath_core(r.left)
            rightMaxVal = longestUnvpath_core(r.right)
            if r.left and r.right and r.left.val == r.right.val and r.val == r.left.val:
                self.resMax = max(self.resMax, leftMaxVal+rightMaxVal+2)

            if r.left and r.left.val == r.val:
                temRes = max(temRes, leftMaxVal + 1)
            if r.right and r.right.val == r.val:
                temRes = max(temRes, rightMaxVal + 1)

            self.resMax = max(temRes, self.resMax)

            return temRes


        longestUnvpath_core(root)
        return self.resMax


# -----
    def arrowLength(self, root):
        '''返回从root延伸而出的最长同值箭头的长度'''
        res = []
        for sub in [root.left, root.right]:
            if sub:
                tmp = self.arrowLength(sub)
                if sub.val == root.val:
                    res.append(1 + tmp)
        if res:
            self.ans = max(self.ans, sum(res))  # 对空集求和结果为0
            return max(res)
        return 0

    def longestUnivaluePath2(self, root: TreeNode) -> int:
        self.ans = 0
        if root:  # 注意空结点
            self.arrowLength(root)  # 本身就是对于树的一次dfs
        return self.ans


# ------
    def longestUnivaluePath3(self, root: TreeNode) -> int:
        self.longest = 0

        def traverse(node, p):
            if not node:
                return 0
            l, r = traverse(node.left, node.val), traverse(node.right, node.val)
            self.longest = max(self.longest, l + r)
            return 1 + max(l, r) if node.val == p else 0

        traverse(root, None)
        return self.longest
