class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        for i in range(len(A)):
            if A[i][0] == 1:
                pass
            else:
                for index in range(len(A[i])):
                    A[i][index] = 1 - A[i][index]

        for i in range(len(A[0])):
            sum = 0
            for j in range(len(A)):
                sum += A[j][i]
            if sum > len(A)//2:
                pass
            else:
                for j in range(len(A)):
                    A[j][i] = 1 - A[j][i]
        # print(A)
        res = 0
        for each in A:
            each_Str = "".join(map(str, each))
            # print(each_Str)
            res += int(each_Str,2)
        return res

    def matrixScore2(self, A: 'List[List[int]]') -> 'int':
        M, N = len(A), len(A[0])
        # 第0列全部变成1
        res = M
        for j in range(1, N):
            # 统计第j列 (1<=j<N) 1的个数
            ones = sum(A[i][j] == A[i][0] for i in range(M))
            # 如果1的个数少于0的个数就翻转，同时更新最终结果
            res = (res << 1) + max(ones, M - ones)
        return res


A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
s = Solution()
print(s.matrixScore(A))