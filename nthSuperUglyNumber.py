from heapq import *


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 0:
            return 0
        Ugly_list = [-1 for _ in range(n)]
        Ugly_list[0] = 1
        nextUgly_index = 1
        primes_list = [0 for _ in range(len(primes))]


        while(nextUgly_index < len(Ugly_list)):
            min_number = float('inf')
            for i in range(len(primes)):
                if min_number > Ugly_list[primes_list[i]] * primes[i]:
                    min_number = Ugly_list[primes_list[i]] * primes[i]

            if min_number != float('inf'):
                Ugly_list[nextUgly_index] = min_number

            for i in range(len(primes)):
                while(Ugly_list[primes_list[i]] * primes[i] <= Ugly_list[nextUgly_index]):
                    primes_list[i] += 1
            nextUgly_index += 1

        return Ugly_list[-1]

    def nthSuperUglyNumber2(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap, uglies, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
        uglies[0] = 1

        for k, p in enumerate(primes):
            heappush(heap, (p, k))

        for i in range(1, n):
            uglies[i], k = heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]


if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    s = Solution()
    print(s.nthSuperUglyNumber(n, primes))
    print(s.nthSuperUglyNumber2(n, primes))

