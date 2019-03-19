class Solution:
    def findLength(self, A, B) -> int:
        if not A or not B:
            return 0
        res = 0
        Dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        for i in range(1, len(B) + 1):
            for j in range(1, len(A) + 1):
                if A[j-1] == B[i - 1]:
                    Dp[i][j] = Dp[i-1][j-1] + 1
                else:
                    Dp[i][j] = 0
                if  Dp[i][j] > res:
                    res = Dp[i][j]

        return res



if __name__ == "__main__":
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    s = Solution()
    print(s.findLength(A, B))

    A2= [0, 1, 1, 1, 1]
    B2= [1, 0, 1, 0, 1]
    print(s.findLength(A2, B2))