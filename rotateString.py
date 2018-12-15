class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            tem = A[i:] + A[:i]
            if tem == B:
                return True
        return False

    def rotateString2(self, A, B):
        return len(A) == len(B) and B in A + A


s  =Solution()
print(s.rotateString2(A = 'abcde', B = 'cdeab'))
