class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        if not A or not B:
            return 0

        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        print(dp)
        max_num = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                # max_num = max(max_num, dp[i][j])

        # print(dp)
        return dp[-1][-1]




A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
s = Solution()
print(s.maxUncrossedLines(A, B))