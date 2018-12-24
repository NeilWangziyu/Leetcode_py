class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # if len(A) < 2:
        #     return 0

        A.sort()

        if A[0] == A[-1]:
            return 0
        else:
            smaller = A[0] + K
            bigger = A[-1] - K
            if smaller >= bigger:
                return 0
            else:
                return bigger - smaller