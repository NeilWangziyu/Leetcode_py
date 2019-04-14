# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def split_str(str, num):
            split_anchor = '-' * num
            if not str:
                return None

            if "-" not in str:
                val = int(str)
                return TreeNode(val)
            else:
                find_split_index = []
                for i in range(len(str)):
                    if str[i:i + num] == split_anchor:
                        if str[i - 1].isdigit() and str[i + num].isdigit():
                            find_split_index.append(i)
                # print(find_split_index)
                if len(find_split_index) == 2:
                    str_left = str[find_split_index[0] + num:find_split_index[1]]
                    str_right = str[find_split_index[1] + num:]
                    val_Str = int(str[:find_split_index[0]])
                    # print(str_left, str_right, val_Str)
                elif len(find_split_index) == 1:
                    str_left = str[find_split_index[0] + num:]
                    str_right = None
                    val_Str = int(str[:find_split_index[0]])
                    # print(str_left, str_right, val_Str)
                else:
                    str_left = None
                    str_right = None
                    val_Str = int(str)
                    # print(str_left, str_right, val_Str)
                root = TreeNode(val_Str)
                root.left = split_str(str_left, num + 1)
                root.right = split_str(str_right, num + 1)
                return root

        root = split_str(S, 1)
        return root

if __name__ == "__main__":
    S = "1-2--3--4-5--6--7"
    s = Solution()
    print(s.recoverFromPreorder(S))





    # split_str("1-2--3--4-5--6--7", 1)
