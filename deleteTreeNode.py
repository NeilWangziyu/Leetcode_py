# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.deleteNode(root, key)

    def findmin(self, r):
        if not r.left:
            return r
        else:
            return self.findmin(r.left)

    def deleteMin(self, r):
        if not r.left:
            return r.right
        r.left = self.deleteMin(r.left)
        return r

    def deleteNodeCode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNodeCode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNodeCode(root.right, key)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.findmin(root.right)
                successor.right = self.deleteMin(root.right)
                successor.left = root.left
            return successor
    # ---------------------
    def deleteNode2(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        '''
        find the node, which val equals to key, and the smallest node in the right child, use this child's node replace the key node.
        '''
        if root is None:
            return root

        if root.val == key:
            if root.left is None and root.right is None:
                return None

            if root.left and root.right:
                p = root.right
                if p.left is None:
                    p.left = root.left
                    return p

                q = p.left  # q stand the next traverse of root
                while q.left:
                    p = q  # if there have smaller node, find the deepest left node
                    q = q.left
                p.left = q.right

                q.left = root.left
                q.right = root.right
                return q

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)

        return root



if __name__ == "__main__":
    s = Solution()
    print(s.deleteNode())


