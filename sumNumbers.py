# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    total = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def return_all_number(root, prev):
            if not root.left and not root.right:
                res_list.append(prev + str(root.val))
            if root.left:
                return_all_number(root.left, prev + str(root.val))
            if root.right:
                return_all_number(root.right, prev + str(root.val))

        if not root:
            return 0

        res_list = []
        return_all_number(root, "")
        print(res_list)
        res = 0
        for each in res_list:
            res += int(each)
        return res

