class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [[]]
        res = []
        check_level = [root]
        count = 0
        while (check_level):
            this_level = []
            next_level = []
            found = False

            for each in check_level:
                if each != "":
                    found = True
                    this_level.append(str(each.val))
                    if each.left:
                        next_level.append(each.left)
                    else:
                        next_level.append("")
                    if each.right:
                        next_level.append(each.right)
                    else:
                        next_level.append("")
                else:
                    this_level.append("")
                    next_level += ["", ""]
            if found:
                check_level = next_level
                count += 1
                res.append(this_level)
            else:
                check_level = []

        res_matrix = [["" for _ in range(2 ** count - 1)] for _ in range(count)]
        if count == 1:
            return res
        # print(res)
        for i in range(len(res)):
            if i == 0:
                res_matrix[i][2 ** (count - (i + 1)) - 1] = res[i][0]
            else:
                this_level = res[i]
                val_num = len(this_level)

                pos = 2 ** (count - (i + 1)) - 1
                for index, each in enumerate(this_level):
                    res_matrix[i][pos] = each
                    pos += (2 ** (count - (i + 1)) - 1) * 2 + 1 + 1
        return res_matrix

    def printTree2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        if not root:
            return [""]

        def getDepth(_root):
            if not _root:
                return 0
            return 1 + max(getDepth(_root.left), getDepth(_root.right))

        d = getDepth(root)
        w = 2 ** d - 1

        recs = [["" for _ in range(w)] for _ in range(d)]

        def insert(_root, d, pos):
            recs[-d - 1][pos] = str(_root.val)
            if _root.left:
                insert(_root.left, d - 1, pos - 2 ** (d - 1))
            if _root.right:
                insert(_root.right, d - 1, pos + 2 ** (d - 1))

        insert(root, d - 1, 2 ** (d - 1) - 1)
        return recs