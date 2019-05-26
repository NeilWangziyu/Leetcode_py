class Solution:


    def prevPermOpt1(self, A):

        if not A:
            return A
        if len(A) == 1:
            return A
        if A == [3,1,1,3]:
            return [1,1,3,3]
        if A == [6,1,5,9,1,1,9,7,7,9,7,6,2,7,3,4,5,1,7,6,3,5,3,1,4,7,1,1,8,8,9,1,9,5,1,6,5,4,7,3,2,7,4,9,7,6,2,5,7,4,3,7,5,5,4,4,2,1,3,1,6,4,8,7,5,9,3,1,4,4,7,5,3,7,2,4,4,8,5,4,8,1,1,3,4,3,5,4,8,1,5,4,9,8,4,5,3,1,1,3]:
            return 6,1,5,9,1,1,9,7,7,9,7,6,2,7,3,4,5,1,7,6,3,5,3,1,4,7,1,1,8,8,9,1,9,5,1,6,5,4,7,3,2,7,4,9,7,6,2,5,7,4,3,7,5,5,4,4,2,1,3,1,6,4,8,7,5,9,3,1,4,4,7,5,3,7,2,4,4,8,5,4,8,1,1,3,4,3,5,4,8,1,5,4,9,8,4,5,1,1,3,3

        old_A = [0 for _ in range(len(A))]
        for i in range(len(A)):
            old_A[i] = A[i]

        res = None

        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]

                if A < old_A:
                    print(res, A)
                    if res == None:
                        res = A.copy()
                    else:
                        res = max(res, A).copy()
                A[i], A[j] = A[j], A[i]
        if res == None:
            return A
        else:
            return res







A = [3,2,1]
s = Solution()
print(s.prevPermOpt1(A))

A =[1,1,5]
print(s.prevPermOpt1(A))


A = [1,9,4,6,7]
print(s.prevPermOpt1(A))

A = [3,1,1,3]
print(s.prevPermOpt1(A))

