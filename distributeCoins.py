# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        not finish yet
        """
        if root == None:
            return 0
        return abs(self.coins(root)-self.sz(root))+self.distributeCoins(root.left)+self.distributeCoins(root.right)


    def sz(self, root):
        if root == None:
            return 0
        return 1+ self.sz(root.left)+self.sz(root.right)


    def coins(self, root):
        if root == None:
            return 0

        return root.val + self.coins(root.left)+self.coins(root.right)



