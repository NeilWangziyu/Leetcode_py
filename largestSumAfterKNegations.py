class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        hasZero = False
        for index, a in enumerate(A):
            if a < 0 and K > 0:
                A[index] = -a
                K -= 1
            if a == 0:
                hasZero = True
        if hasZero or K % 2 == 0:
            return sum(A)
        return sum(A) - 2 * min(A)