# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check_Subtree(s_r, t_r):

            if not s_r and not t_r:
                return True
            elif not s_r or not t_r:
                return False
            else:
                if s_r.val != t_r.val:
                    return False
                else:
                    return check_Subtree(s_r.left, t_r.left) and check_Subtree(s_r.right, t_r.right)

        if not t and not s:
            return True

        if not s:
            return False

        if not t:
            return False

        result = False
        if s.val == t.val:
            result = check_Subtree(s.left, t.left) and check_Subtree(s.right, t.right)
        if not result:
            result = self.isSubtree(s.left, t)
        if not result:
            result = self.isSubtree(s.right, t)

        return result

    def isSubtree2(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 另一种思路，分别将两棵树序列化
        # 然后根据序列化的结果判断是否存在子树
        # 感觉这个就是python的方法了，非常有意思
        s_serialize = self.serialize(s)
        t_serialize = self.serialize(t)

        if t_serialize in s_serialize:
            return True
        else:
            return False

    def serialize(self, root):
        if root is None:
            return []

        def pre_order(root):
            if root:
                result.append('^' + str(root.val))
                pre_order(root.left)
                pre_order(root.right)
            else:
                result.append('^#')

        result = []
        pre_order(root)

        return ','.join(result)

if __name__ =="__main__":
    pass