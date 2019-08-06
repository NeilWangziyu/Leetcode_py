class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K == 1:
            return 0
        if K == 2:
            return 1

        tem = "0"
        for i in range(N - 1):
            new_tem = ""
            for each in tem:
                if each == '0':
                    new_tem += "01"
                else:
                    new_tem += "10"
            tem = new_tem
        return int(tem[K - 1])

    def kthGrammar2(self, N: int, K: int) -> int:
        if K == 1:
            return 0
        if K == 2:
            return 1

        a = self.kthGrammar(N-1, (K+1)//2)
        b = -(a-1)
        if K%2==1:
            return a
        else:
            return b

# //附图
# //序号
# //              1
# //          /        \
# //      1                2
# //    /   \            /    \
# //  1       2        3       4
# // / \     /  \     /  \    / \
# //1   2   3    4   5    6  7   8
#
# //01排列
# //              0
# //          /        \
# //      0                1
# //    /   \            /    \
# //  0       1        1       0
# // / \     /  \     /  \    / \
# //0   1   1    0   1    0  0   1