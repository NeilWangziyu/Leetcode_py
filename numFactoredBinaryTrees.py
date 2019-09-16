from typing import List
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        # 超时
        def core(root_val, A):
            res = 1
            for each in A:
                if root_val/each in A:
                    res += core(each, A) * core(root_val/each, A)
            return res % (10**9 + 7)
        A = set(A)
        r = 0
        for each in A:
            r += core(each, A)
        return r % (10**9 + 7)

    def numFactoredBinaryTrees2(self, A: List[int]) -> int:
        sum = 0
        dp = {}
        for each in A:
            dp[each] = 1
        A.sort()
        for i in range(len(A)):
            cur = A[i]
            for j in range(i):
                if cur / A[j] in dp:
                    dp[cur] = dp[cur] + dp[A[j]] * dp[cur/A[j]]
            sum = (sum + dp[cur]) % (10**9 + 7)

        return sum


s = Solution()
print(s.numFactoredBinaryTrees([2,4]))
print(s.numFactoredBinaryTrees([2, 4, 5, 10]))

print(s.numFactoredBinaryTrees2([2,4]))
print(s.numFactoredBinaryTrees2([2, 4, 5, 10]))