import copy
class Solution:
    def isArmstrong(self, N: int) -> bool:
        if N == 1:
            return True

        k = len(str(N))
        res = 0
        x = copy.copy(N)
        while(x):
            res += (x%10) ** k
            x = x // 10
        print(res, N)
        return res == N

s = Solution()
print(s.isArmstrong(153))
print(s.isArmstrong(123))


