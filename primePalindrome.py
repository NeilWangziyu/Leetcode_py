import math


class Solution:
    # 超时
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def isPalindrome(N):
            if len(N) == 1:
                return True
            else:
                str_N = N[::-1]
                if str_N != N:
                    return False
                else:
                    return True

        def isPrime(N):
            if N == 1:
                return True
            check = 2
            while (check <= math.sqrt(N)):
                if N % check == 0:
                    return False
                check += 1
            return True

        if N == 0:
            return 2
        if N == 1:
            return 2

        while (True):
            if isPrime(N) and isPalindrome(str(N)):
                return N
            if N > 11 and len(str(N)) % 2 == 0:
                N = 10 ** (len(str(N))) + 1
            else:
                N += 1


class Solution2:
    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True if num > 1 else False

        def isPalindrome(num):
            return str(num) == str(num)[::-1]

        while True:
            if isPalindrome(N) and isPrime(N):
                return N
            else:
                if N > 11 and len(str(N)) % 2 == 0:
                    N = 10 ** len(str(N)) + 1
                else:
                    N += 1


if __name__ == "__main__":
    s = Solution()
    print(s.primePalindrome(1000))





