class Solution:
    def tribonacci0(self, n: int) -> int:
        # 超时
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)



    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(1, n):
            ret = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = ret
        return ret