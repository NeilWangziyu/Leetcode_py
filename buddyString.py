class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        differ = []
        for i in range(len(A)):
            if A[i] != B[i]:
                differ.append(i)


        if differ == []:
            if len(A) - len(set(A)) > 0:
                return True
            else:
                return False

        if len(differ)==2:
            if A[differ[0]] == B[differ[1]] and A[differ[1]] == B[differ[0]]:
                return True
            else:
                return False
        else:
            return False






s = Solution()
print(s.buddyStrings("abc", "acb"))
print(s.buddyStrings("ab", "ab"))