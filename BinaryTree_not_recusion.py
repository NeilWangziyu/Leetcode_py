# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class recusion:
    def inorderTraversal(self, root):
        """中序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root != None:
            if (root.left):
                result += (self.inorderTraversal(root.left))
            result += [root.val]
            if (root.right):
                result += (self.inorderTraversal(root.right))
        else:
            return []
        return result


    def preorderTraversal(self, root):
        """前序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return []
        if root == []:
            return []
        else:
            result += [root.val]
            if root.left:
                result += self.preorderTraversal(root.left)
            if root.right:
                result += self.preorderTraversal(root.right)
        return result


    def postorderTraversal(self, root):
        """后序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        if root:
            if root.left:
                list += self.postorderTraversal(root.left)
            if root.right:
                list += self.postorderTraversal(root.right)
            list += [root.val]
        return list



class not_recusion:
    def preorderTraversal(self, root):
        """前序遍历，用stack，先进root，再进left，right
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res_list = []
        if not root:
            return res_list
        tree_stack = []
        tree_stack.append(root)

        while (tree_stack):
            this_node = tree_stack.pop()
            # 取出栈顶
            print(this_node.val)
            res_list.append(this_node.val)
            if this_node.right:
                tree_stack.append(this_node.right)
            if this_node.left:
                tree_stack.append(this_node.left)
        return res_list



    def inorderTraversal(self, root):
        # 中序遍历
        res_list = []
        if not root:
            return res_list
        tree_stack = []
        while (root or tree_stack):
            if root:
                tree_stack.append(root)
                root = root.left
            else:
                root = tree_stack.pop()
                res_list.append(root.val)
                root = root.right
        return res_list


    def postorderTraversal(self, root):
        """后序遍历，需要两个stack,或者说将res取反
        :type root: TreeNode
        :rtype: List[int]
        """
        tem_stack = []
        res_list = []
        if not root:
            return res_list
        tem_stack.append(root)
        while(tem_stack):
            this_node = tem_stack.pop()
            if this_node.left:
                tem_stack.append(this_node.left)
            if this_node.right:
                tem_stack.append(this_node.right)
            res_list.append(this_node.val)
        res_list.reverse()
        return res_list










