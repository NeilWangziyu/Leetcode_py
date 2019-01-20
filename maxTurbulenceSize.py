class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 2:
            return len(A)
        if len(A) == 2:
            if A[0] != A[1]:
                return 2
            else:
                return 1

        # DP = [0 for _ in range(len(A))]
        # FLAG = [0 for _ in range(len(A))]
        # # 0:both
        # #  1:若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]
        # # -1：或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]

        DP_1 = [0 for _ in range(len(A))]
        DP_2 = [0 for _ in range(len(A))]
        DP_1[0] = 1
        DP_2[0] = 1
        for i in range(len(A)-1):
            print(A[i+1], A[i])
            if i % 2 == 0:
                if A[i] < A[i+1]:
                    DP_1[i+1] += DP_1[i] + 1
                    DP_2[i+1] = 1
                elif A[i] > A[i+1]:
                    DP_2[i+1] += DP_2[i] + 1
                    DP_1[i+1] = 1
                else:
                    DP_1[i+1] = 1
                    DP_2[i+1] = 1

            else:
                if A[i] > A[i+1]:
                    DP_1[i+1] += DP_1[i] + 1
                    DP_2[i+1] = 1
                elif A[i] < A[i+1]:
                    DP_2[i+1] += DP_2[i] + 1
                    DP_1[i+1] = 1
                else:
                    DP_1[i+1] = 1
                    DP_2[i+1] = 1

        print(DP_1, DP_2)
        return max(max(DP_2), max(DP_1))




A = [9,4,2,10,7,8,8,1,9]
# A = [37,199,60,296,257,248,115,31,273,176]
s = Solution()
print(s.maxTurbulenceSize(A))