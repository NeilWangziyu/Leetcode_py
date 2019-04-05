# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        注意p,q必然存在树内, 且所有节点的值唯一!!!
        递归思想, 对以root为根的(子)树进行查找p和q, 如果root == null || p || q 直接返回root
        表示对于当前树的查找已经完毕, 否则对左右子树进行查找, 根据左右子树的返回值判断:
        1. 左右子树的返回值都不为null, 由于值唯一左右子树的返回值就是p和q, 此时root为LCA
        2. 如果左右子树返回值只有一个不为null, 说明只有p和q存在与左或右子树中, 最先找到的那个节点为LCA
        3. 左右子树返回值均为null, p和q均不在树中, 返回null
        """
        if not root or root==p or root ==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right :
            return root
        if not left:
            return right
        else:
            return left

    def findPath(self, root, p, path):
        if root.val == p.val:
            return True
        if root.left:
            path.append(root.left)
            if self.findPath(root.left, p, path):
                return True
            else:
                path.pop()
        if root.right:
            path.append(root.right)
            if self.findPath(root.right, p, path):
                return True
            else:
                path.pop()
        return False
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        # 类似于多叉树的方法，返回，寻找list
        """
        path_p, path_q = [root], [root]
        self.findPath(root, p, path_p)
        self.findPath(root, q, path_q)
        n_min = min(len(path_p), len(path_q))
        for i in range(n_min):
            if path_p[i].val == path_q[i].val:
                ans = path_p[i]
        return ans

    # 如果是二叉树，则可以比较root.val和两个值