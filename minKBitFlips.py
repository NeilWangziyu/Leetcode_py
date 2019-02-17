class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        """
        ?????
        做不来啊呜呜呜呜呜呜
        :param A:
        :param K:
        :return:
        """
        n = len(A)
        index = []

        def check(i):
            print(index)
            print("check: ", i)
            while index and i - index[0] >= K:
                index.pop(0)
            n = len(index)
            if n & 1:
                A[i] ^= 1

        ans = 0
        for i in range(n - K + 1):
            check(i)
            if A[i] == 0:
                A[i] = 1
                ans += 1
                index.append(i)

        for i in range(n - K + 1, n):
            check(i)


        if all(A):
            # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
            return ans
        else:
            return -1




A = [0, 0, 0, 1, 0, 1, 1, 0]
K = 3

s = Solution()
print(s.minKBitFlips(A,  K))