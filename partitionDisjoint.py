from typing import List

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        largest = [-1 for _ in range(len(A))]
        smallest = [-1 for _ in range(len(A))]
        largest[0] = A[0]
        smallest[len(A) - 1] = A[-1]

        for i in range(1, len(A)):
            largest[i] = max(A[i], largest[i - 1])

        for i in range(len(A) - 2, -1, -1):
            smallest[i] = min(A[i], smallest[i + 1])

        # print(largest)
        # print(smallest)
        for i in range(len(A)):
            if largest[i] <= smallest[i + 1]:
                return i + 1

    def partitionDisjoint2(self, A: List[int]) -> int:
        # 其实应该是一遍通过
        lmaxv = A[0]
        maxv = A[0]
        l = 0
        for i in range(len(A)):
            if A[i] < lmaxv:
                lmaxv = maxv
                l = i
            elif A[i] > maxv:
                maxv = A[i]
        return l + 1


