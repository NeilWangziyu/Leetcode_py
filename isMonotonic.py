class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        i = 1
        while (A[i] - A[i - 1] == 0):
            i = i + 1
            if i == len(A):
                return True

        prev = A[i] - A[i - 1]
        print(prev)

        for j in range(i, len(A)):
            print(j)
            if (A[j] - A[j - 1]) * prev < 0:
                return False
            else:
                if A[j] - A[j - 1] != 0:
                    prev = A[j] - A[j - 1]
        return True

    def isMonotonic2(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))


A  = [1,3,2]

s =Solution()
print(s.isMonotonic(A))
