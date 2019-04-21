class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        if L == 0 and M == 0:
            return 0
        L_list = []
        M_list = []
        init = 0
        for i in range(len(A)):
            if i < L-1:
                init += A[i]
            elif i == L-1:
                init += A[i]

                L_list.append(init)
            else:
                init -= A[i-L]
                init += A[i]
                L_list.append(init)

        init = 0
        for i in range(len(A)):
            if i < M-1:
                init += A[i]
            elif i == M-1:
                init += A[i]

                M_list.append(init)
            else:
                init -= A[i-M]
                init += A[i]
                M_list.append(init)
        # print(L_list)
        # print(M_list)
        res = 0
        for i in range(len(L_list)):
            for j in range(len(M_list)):
                if i > j+M-1 or j>i+L-1:
                    if L_list[i] + M_list[j] > res:
                        res = L_list[i] + M_list[j]
        return res


A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L = 3
M = 2
s = Solution()
print(s.maxSumTwoNoOverlap(A, L, M))


A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
print(s.maxSumTwoNoOverlap(A, L, M))

