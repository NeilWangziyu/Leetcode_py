class Solution:
    def isIdealPermutation(self, A) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) >= 2:
                return False
        return True

    def isIdealPermutation2(self, A) -> bool:
        for i in range(len(A)):
            if ((A[i] - i) * (A[i] - i) > 1):
                return False
        return True


S = Solution()
print(S.isIdealPermutation(A=[1,2,0]))