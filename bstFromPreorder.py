# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                root.left = self.bstFromPreorder(preorder[1:i])
                root.right = self.bstFromPreorder(preorder[i:])
                return root
        root.left = self.bstFromPreorder(preorder[1:])
        return root




preorder = [8,5,1,7,10,12]
s = Solution()
print(s.bstFromPreorder(preorder))