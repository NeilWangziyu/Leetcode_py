import numpy as np
import scipy.signal

class Solution:
    def maxRotateFunction(self, A):

        """
        错位相减
        :type A: List[int]
        :rtype: int
        """
        h = list(range(len(A)))
        A = A[1:] + A

        max = -float('inf')

        for i in range(len(h)):
            res = sum(A[i+c] * h[c] for c in range(len(h)))
            # print(res)
            if res > max:
                max =res
        return max

    def maxRotateFunction1(self, A):
        if len(A) == 0:
            return 0

        sum = 0
        F = 0

        for i in range(len(A)):
            sum += A[i]
            F += i*A[i]
        F_max = F


        for i in range(len(A)-1, 0, -1):
            F = F + sum - len(A)*A[i]
            if F > F_max:
                F_max = F
        return F_max





A = [99,2,3,4,5,6,7,8,9,10]

s = Solution()
print(s.maxRotateFunction1(A))