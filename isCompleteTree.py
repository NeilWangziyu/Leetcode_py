# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        while(stack):
            full = True
            found_next = False
            next_level = []
            for each in stack:
                if type(each) != TreeNode:
                    next_level.append('#')
                    next_level.append('#')
                    full = False
                else:
                    # print(each.val, full)
                    if full == False:
                        return False
                    if each.left:
                        next_level.append(each.left)
                        found_next = True
                    else:
                        next_level.append("#")
                    if each.right:
                        next_level.append(each.right)
                        found_next = True
                    else:
                        next_level.append("#")
            if found_next:
                if full == False:
                    # print(len(set(next_level)))
                    return  False
                stack = next_level
                # print(next_level)
            else:
                break
        return True

    def isCompleteTree2(self, root):
        # 这个idea和我的是一样的
        import collections
        queue, f = collections.deque([root]), 0

        while queue:
            temp = queue.popleft()

            if f == 1 and temp != '*':
                return False

            if f == 0 and temp == '*':
                f = 1

            if temp != '*' and temp.left:
                queue.append(temp.left)
            elif temp != '*' and temp.left is None:
                queue.append('*')

            if temp != '*' and temp.right:
                queue.append(temp.right)
            elif temp != '*' and temp.right is None:
                queue.append('*')

        return True

    def isCompleteTree3(self, root: TreeNode) -> bool:

        def dfs(root):
            if root:
                return max(dfs(root.left) + 1, dfs(root.right) + 1)
            return 0

        depth = dfs(root)
        before = 0;
        ans = True;
        count = 0;
        if depth == 1:
            return True

        def counter(root, layer):
            nonlocal count
            if root:
                if layer == depth - 1:
                    count += 1
                counter(root.left, layer + 1)
                counter(root.right, layer + 1)

        counter(root, 1)
        # print(count,depth)
        if count != pow(2, depth - 2):
            return False;

        def check(root, layer):
            nonlocal ans, before
            if layer == depth - 1:
                if before == 0:
                    if root.left:
                        if root.right:
                            before = 1
                        else:
                            before = 2
                    else:
                        if root.right:
                            ans = False
                        else:
                            before = 2
                elif before == 1:
                    if root.left:
                        if root.right:
                            before = 1
                        else:
                            before = 2
                    else:
                        if root.right:
                            ans = False
                        else:
                            before = 2
                elif before == 2:
                    # print(root.val)
                    if root.left or root.right:
                        ans = False
            if root and ans:
                check(root.left, layer + 1)
                check(root.right, layer + 1)

        check(root, 1)
        return ans;


