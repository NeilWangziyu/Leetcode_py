class Solution:
    def maxSumAfterPartitioning(self, A, K):
        """
        这题做不来

        """
        N = len(A)
        dp = [0 for _ in range(N+1)]
        for i in range(N):
            t = -float('inf')
            j = i - 1
            while(j>=-1 and i-j<=K):
                t = max(t, A[j+1])
                dp[i+1] = max(dp[j+1]+(i-j)*t, dp[i+1])
                j -= 1

        return dp[N]

s = Solution()
A = [1,15,7,9,2,5,10]
K = 3
print(s.maxSumAfterPartitioning(A, K))
