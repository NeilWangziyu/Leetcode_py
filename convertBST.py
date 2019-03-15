# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    preNUm = 0

    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        以右->根->左的顺序遍历二叉树，将遍历顺序的前一个结点的累加值记录起来，和当前结点相加，得到当前结点的累加值。
        """

        def unpreorder(root):
            if not root:
                return
            unpreorder(root.right)
            root.val += self.preNUm
            self.preNUm = root.val
            unpreorder(root.left)

        unpreorder(root)
        return root


    def convertBST2(self, root):
        """
        NOT
        :param root:
        :return:
        """
        if not root:
            return root

        stack = []
        check_node = root
        while (check_node != None or stack != []):
            while (check_node):
                stack.append(check_node)
                check_node = check_node.right

            check_node = stack.pop()
            check_node.val += self.preNUm
            self.preNUm = check_node.val
            if check_node.left:
                check_node = check_node.left
            else:
                check_node = None
        return root