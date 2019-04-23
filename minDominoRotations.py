class Solution:
    def minDominoRotations(self, A, B) -> int:
        from collections import Counter
        # 0:A, 1:B
        num_hash = {}
        num_numA = {}
        num_numB = {}

        for i in range(1, 7):
            num_hash[i] = set()
            num_numA[i] = 0
            num_numB[i] = 0

        for i in range(len(A)):
            num_hash[A[i]].add(i)
            num_hash[B[i]].add(i)


            num_numA[A[i]] += 1
            num_numB[B[i]] += 1

        # print(num_hash)
        # print(num_num)

        res = -1
        for index in num_hash.keys():
            if len(num_hash[index]) == len(A):
                if res == -1:
                    res = min(len(A)-num_numB[index], len(A)-num_numA[index])
                else:
                    res = min(res, min(len(A)-num_numB[index], len(A)-num_numA[index]))

        return res


    def minDominoRotations2(self, A, B):
        for x in range(1, 7):
            if all(x == a or x == b for a, b in zip(A, B)):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1


A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
s = Solution()
print(s.minDominoRotations(A, B))

A = [1,2,1,1,1,2,2,2]
B = [2,1,2,2,2,2,2,2]
print(s.minDominoRotations(A, B))





