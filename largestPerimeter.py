class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        A.sort(reverse=True)
        print(A)
        max_length = 0
        for i in range(2, len(A)):
            if A[i-2] < A[i-1] + A[i]:
                return A[i-2] + A[i-1] + A[i]
        return max_length



A = [3,2,3,4]
s = Solution()
print(s.largestPerimeter(A))