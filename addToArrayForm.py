class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if len(A) < len(str(K)):
            A = [0] * (len(str(K)) - len(A)) + A

        c = 0
        for i in range(len(A) - 1, -1, -1):
            tem = A[i] + K % 10 + c
            A[i] = tem % 10
            c = tem // 10

            K = K // 10

        if c != 0:
            A = [1] + A
        return A