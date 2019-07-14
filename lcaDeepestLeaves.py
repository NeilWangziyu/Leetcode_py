# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if not root.left and not root.right:
            return root

        self.lowest = []
        self.deepest = 0

        self.find_deepest_node(root, level=0)

        print(len(self.lowest))
        if not self.lowest:
            return root

        else:
            return self.LCA(root, self.lowest)

    def find_deepest_node(self,root, level):
        if not root:
            return
        if root.left or root.right:
            self.find_deepest_node(root.left, level+1)
            self.find_deepest_node(root.right, level+1)
        else:
            if level == self.deepest:
                self.lowest.append(root)
            elif level > self.deepest:
                self.deepest = level
                self.lowest = [root]
            return


    def LCA(self, root, node_list):
        if not root or root in node_list:
            return root
        left = self.LCA(root.left, node_list)
        right = self.LCA(root.right, node_list)
        if left and right:
            return root
        if not left:
            return right
        else:
            return left