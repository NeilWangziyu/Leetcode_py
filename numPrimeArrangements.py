class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n <= 2:
            return 1
#         find all number of prime
        check_num = [i for i in range(n+1)]
        check_num[0] = -1
        check_num[1] = -1

        for i in range(len(check_num)):
            if check_num[i] != -1:
                k = 2
                while(check_num[i] * k <= n):
                    check_num[i*k] = -1
                    k += 1
        c = 0
        for each in check_num:
            if each != -1:
                c += 1

        other = n - c
        return self.func(c) * self.func(other) % (10**9+7)

    def func(self, n):
        if n == 1:
            return 1
        else:
            return n * self.func(n-1)


s = Solution()
n = 100
print(s.numPrimeArrangements(n))



