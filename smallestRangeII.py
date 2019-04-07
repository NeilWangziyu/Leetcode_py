class Solution:
    def smallestRangeII(self, A, K):
        # 那么整个 A 的最大值只能是 A1 尾或 A2 尾，最小值只能是 A1 头或 A2 头，比较这4个值就可以求得差值。
        if not A:
            return 0
        if len(A) == 1:
            return 0
        A.sort()
        res = abs(A[-1] - A[0])
        for i in range(1, len(A)):
            minu = min(A[0] + K, A[i] - K)
            maxu = max(A[i - 1] + K, A[len(A) - 1] - K)
            res = min(res, maxu - minu)
        return res







A = [1]
K = 0
s = Solution()
print(s.smallestRangeII(A, K))
