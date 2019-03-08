# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric_old(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list_left = []

        def return_value_left(root):
            if root == None:
                return None
            if root.left != None:
                list_left.append(return_value_left(root.left))
            else:
                list_left.append(None)
            if root.right != None:
                list_left.append(return_value_left(root.right))
            else:
                list_left.append(None)
            list_left.append(root.val)

        list_right = []

        def return_value_right(root):
            if root == None:
                return None
            if root.right != None:
                list_right.append(return_value_right(root.right))
            else:
                list_right.append(None)
            if root.left != None:
                list_right.append(return_value_right(root.left))
            else:
                list_right.append(None)
            list_right.append(root.val)

        return_value_left(root)
        print(list_left)
        # return_value_right(root)
        return_value_right(root)
        print(list_right)
        if list_right == list_left:
            return True
        else:
            return False


    def isSymmetric(self, root: TreeNode) -> bool:
        """
        interesting point：构造两种遍历方法
        :param root:
        :return:
        """
        def isSymmetric_core(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            else:
                return isSymmetric_core(root1.left, root2.right) and isSymmetric_core(root1.right, root2.left)

        return isSymmetric_core(root, root)

