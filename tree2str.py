class Solution:
    res = ""
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def pre_search(t):
            if not t:
                self.res += "()"
                return
            else:
                if not t.left and not t.right:
                    self.res += "("
                    self.res += str(t.val)
                    self.res += ")"
                elif not t.left:
                    self.res += "("
                    self.res += str(t.val)
                    self.res += "()"
                    if t.right:
                        pre_search(t.right)
                    self.res += ")"
                else:
                    self.res += "("
                    self.res += str(t.val)
                    pre_search(t.left)
                    if t.right:
                        pre_search(t.right)
                    self.res += ")"

        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)

        pre_search(t)
        print(self.res)
        return self.res[1:-1]

    def tree2str2(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        res = ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            res += '(%s)' % left
        if right:
            res += '(%s)' % right
        return str(t.val) + res



