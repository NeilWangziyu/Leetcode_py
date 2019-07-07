# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        def prune_tree(r):
            if not r:
                return None
            if r.val in to_delete_set:
                return None
            front = r
            stack = [r]
            while(stack):
                c = stack.pop(0)
                if c.left:
                    if c.left.val in to_delete_set:
                        if c.left.left:
                            stack_new_root.append(c.left.left)
                        if c.left.right:
                            stack_new_root.append(c.left.right)
                        c.left = None
                    else:
                        stack.append(c.left)
                if c.right:
                    if c.right.val in to_delete_set:
                        if c.right.left:
                            stack_new_root.append(c.right.left)
                        if c.right.right:
                            stack_new_root.append(c.right.right)
                        c.right = None
                    else:
                        stack.append(c.right)
            return r




        if not root:
            return []
        if not to_delete:
            return [root]

        res = []

        to_delete_set = set(to_delete)
        stack_new_root = [root]

        while(stack_new_root):
            check = stack_new_root.pop(0)
            if check.val in to_delete_set:
                if check.left:
                    stack_new_root.append(check.left)
                if check.right:
                    stack_new_root.append(check.right)
            else:
                pruned = prune_tree(check)
                if pruned:
                    res.append(pruned)


        return res