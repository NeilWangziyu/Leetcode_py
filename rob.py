# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def DFS(root):
            if not root:
                return [0, 0]
            #             左边：抢劫root， 右边：不抢root
            else:
                left = DFS(root.left)
                right = DFS(root.right)
                with_Val = root.val + left[1] + right[1]
                without_Val = max(left) + max(right)
                return [with_Val, without_Val]

        res = DFS(root)
        return max(res)







