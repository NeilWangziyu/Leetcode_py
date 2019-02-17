# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        def find_node(check_root, target, depth, parent):
            if not check_root:
                return [False, depth, parent]
            if check_root.val == target:
                return [True, depth, parent]
            else:
                if find_node(check_root.left, target, depth + 1, check_root.val)[0]:
                    return find_node(check_root.left, target, depth + 1, check_root.val)
                elif find_node(check_root.right, target, depth + 1, check_root.val)[0]:
                    return find_node(check_root.right, target, depth + 1, check_root.val)
                return [False, depth, check_root.val]

        if not root:
            return False
        print(find_node(root, x, 0, None))
        print(find_node(root, y, 0, None))

        x_find = find_node(root, x, 0, None)
        y_find = find_node(root, y, 0, None)
        if x_find[0] == False or y_find[0] == False:
            return False
        elif x_find[1] != y_find[1]:
            return False
        elif x_find[2] == y_find[2]:
            return False
        return True

