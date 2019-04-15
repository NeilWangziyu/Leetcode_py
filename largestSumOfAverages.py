class Solution:
    def largestSumOfAverages(self, A, K) -> float:
        # dp[i][k]
        # 表示前i个数构成k个子数组时的最大平均值, 那么对于所有
        # 0 <= j <= i - 1
        # dp[i][k] = Math.max(dp[i][k], dp[j][k - 1] + (A[j + 1] + ... + A[i + 1]) / (i - j))
        # // 额外记录一个sum数组保存到前i个数的和, 便于计算(A[j+1] + ... + A[i+1]) / (i-j)

        length = len(A)
        dp = [[0 for _ in range(K+1)] for _ in range(length + 1)]
        sum_list = [0 for _ in range(length + 1)]
        for i in range(1, length+1):
            sum_list[i] = sum_list[i-1] + A[i-1]
            dp[i][1] = sum_list[i] / i

        for i in range(1, length + 1):
            for k in range(2, K+1):
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + (sum_list[i]-sum_list[j]) / (i-j))

        print(dp)
        print(sum_list)
        return dp[length][K]




A = [9, 1, 2, 3, 9]
K = 3
s = Solution()
print(s.largestSumOfAverages(A, K))