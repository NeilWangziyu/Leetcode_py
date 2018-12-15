# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    list_node = []
    min_val = None

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(n):
            print(self.list_node)
            if not n:
                return
            for each in self.list_node:
                if abs(each - n.val) < self.min_val:
                    self.min_val = abs(each - n.val)
            self.list_node.append(n.val)
            check(n.left)
            check(n.right)

        if not root:
            return None

        if not root.left and not root.right:
            return None

        self.list_node.append(root.val)
        self.min_val = float('inf')
        check(root.right)
        check(root.left)
        return self.min_val


    def minDiffInBST2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check_val(list, val):
            min = float('inf')
            for each in list:
                if abs(each - val)<min:
                    min = abs(each - val)
            return min

        if not root:
            return None
        if not root.left and not root.right:
            return None

        check_list = [root.val]
        stack = []
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

        res = float('inf')
        while(stack):
            check = stack.pop(0)
            if check.left:
                stack.append(check.left)
            if check.right:
                stack.append(check.right)
            min_this = check_val(check_list, check.val)
            if min_this < res:
                res = min_this
            check_list.append(check.val)
        return res








