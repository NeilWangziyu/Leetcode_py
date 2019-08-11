class Solution:
    def numRollsToTarget0(self, d: int, f: int, target: int) -> int:
        if d * f < target:
            return 0
        if d * f == target:
            return 1
        if d == 1:
            return 1
        res = 0
        for i in range(1, f+1):
            res += self.numRollsToTarget(d-1, f, target-i)
        return res % (10**9+7)


    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # if d * f < target:
        #     return 0
        # if d * f == target:
        #     return 1
        # if d == 1:
        #     return 1
        dp = [[0 for _ in range(target+1)]  for _ in range(d+1)]
        for target_i in range(target + 1):
            for d_i in range(d + 1):
                if d_i*f < target_i:
                    dp[d_i][target_i] = 0
                elif d_i*f == target_i:
                    dp[d_i][target_i] = 1
                elif d_i == 1:
                    dp[d_i][target_i] = 1
                else:
                    res = 0
                    for tem in range(1, f+1):
                        if(target_i - tem > 0):
                            res += dp[d_i-1][target_i - tem]
                    dp[d_i][target_i] = res % (10**9+7)
        return dp[d][target]




s = Solution()
print(s.numRollsToTarget(d = 1, f = 6, target = 3))
print(s.numRollsToTarget(d = 3, f = 2, target = 3))
print(s.numRollsToTarget(d = 2, f = 6, target = 7))
print(s.numRollsToTarget(d = 2, f = 5, target = 10))
print(s.numRollsToTarget(d = 1, f = 2, target = 3))
print(s.numRollsToTarget(d = 30, f = 30, target = 500))

