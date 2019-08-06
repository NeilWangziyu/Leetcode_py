class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        def myPow(x, n):
            if n < 0:
                x, n = 1 / x, -n
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                return myPow(x * x, n // 2)
            else:
                return myPow(x * x, n // 2) * x



        if not b:
            return
        if a == 0 or a == 1:
            return a
        b = int("".join(map(str, b)))

        return myPow(a, b) % 1337

    def superPow2(self, a, b):
        return pow(a, b[-1], 1337) * pow(self.superPow(a, b[:-1]), 10, 1337) % 1337 if len(b) > 0 else 1

    def superPow3(self, a, b):
        s = 0
        for k in b:
            s = s * 10 + k
        return pow(a, s, 1337)

    def superPow4(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int

        """
        if a == 1:
            return a

        def t1(a, b):
            cnt = []
            while b > 1:
                if b % 2:
                    cnt.append(a)
                a = a ** 2 % 1337
                b //= 2
            for num in cnt:
                a = a * num % 1337
            return a

        a %= 1337
        cnt = []
        for num in b[::-1]:
            if num:
                cnt.append(t1(a, num))
            a = t1(a, 10)
        a = 1
        for num in cnt:
            a = a * num % 1337
        return a

    def superPow5(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        欧拉-费马降幂
        a^b %c == a^(b%phi(c)) % c
        phi(c)是欧拉函数，表示小于c的和c互质的数的个数
        c = 1337, phi(c) = 1140
        """
        a = a % 1337
        if a <= 1:
            return a
        while b and b[0] == 0:
            b.pop(0)
        if not b:
            return 1
        n_pow = 0
        for n in b:
            n_pow = (n_pow * 10 + n) % 1140
        if n_pow == 0:  # 7^1140 == 574 不是 1
            n_pow = 1140
        res = 1
        while n_pow > 0:
            if n_pow & 1 == 1:
                res = res * a % 1337
            a = a * a % 1337
            n_pow >>= 1
        return res


if __name__ == "__main__":
    a = 78267
    b = [1,7,7,4,3,1,7,0,1,4,4,9,2,8,5,0,0,9,3,1,2,5,9,6,0,9,9,0,9,6,0,5,3,7,9,8,8,9,8,2,5,4,1,9,3,8,0,5,9,5,6,1,1,8,9,3,7,8,5,8,5,5,3,0,4,3,1,5,4,1,7,9,6,8,8,9,8,0,6,7,8,3,1,1,1,0,6,8,1,1,6,6,9,1,8,5,6,9,0,0,1,7,1,7,7,2,8,5,4,4,5,2,9,6,5,0,8,1,0,9,5,8,7,6,0,6,1,8,7,2,9,8,1,0,7,9,4,7,6,9,2,3,1,3,9,9,6,8,0,8,9,7,7,7,3,9,5,5,7,4,9,8,3,0,1,2,1,5,0,8,4,4,3,8,9,3,7,5,3,9,4,4,9,3,3,2,4,8,9,3,3,8,2,8,1,3,2,2,8,4,2,5,0,6,3,0,9,0,5,4,1,1,8,0,4,2,5,8,2,4,2,7,5,4,7,6,9,0,8,9,6,1,4,7,7,9,7,8,1,4,4,3,6,4,5,2,6,0,1,1,5,3,8,0,9,8,8,0,0,6,1,6,9,6,5,8,7,4,8,9,9,2,4,7,7,9,9,5,2,2,6,9,7,7,9,8,5,9,8,5,5,0,3,5,8,9,5,7,3,4,6,4,6,2,3,5,2,3,1,4,5,9,3,3,6,4,1,3,3,2,0,0,4,4,7,2,3,3,9,8,7,8,5,5,0,8,3,4,1,4,0,9,5,5,4,4,9,7,7,4,1,8,7,5,2,4,9,7,9,1,7,8,9,2,4,1,1,7,6,4,3,6,5,0,2,1,4,3,9,2,0,0,2,9,8,4,5,7,3,5,8,2,3,9,5,9,1,8,8,9,2,3,7,0,4,1,1,8,7,0,2,7,3,4,6,1,0,3,8,5,8,9,8,4,8,3,5,1,1,4,2,5,9,0,5,3,1,7,4,8,9,6,7,2,3,5,5,3,9,6,9,9,5,7,3,5,2,9,9,5,5,1,0,6,3,8,0,5,5,6,5,6,4,5,1,7,0,6,3,9,4,4,9,1,3,4,7,7,5,8,2,0,9,2,7,3,0,9,0,7,7,7,4,1,2,5,1,3,3,6,4,8,2,5,9,5,0,8,2,5,6,4,8,8,8,7,3,1,8,5,0,5,2,4,8,5,1,1,0,7,9,6,5,1,2,6,6,4,7,0,9,5,6,9,3,7,8,8,8,6,5,8,3,8,5,4,5,8,5,7,5,7,3,2,8,7,1,7,1,8,7,3,3,6,2,9,3,3,9,3,1,5,1,5,5,8,1,2,7,8,9,2,5,4,5,4,2,6,1,3,6,0,6,9,6,1,0,1,4,0,4,5,5,8,2,2,6,3,4,3,4,3,8,9,7,5,5,9,1,8,5,9,9,1,8,7,2,1,1,8,1,5,6,8,5,8,0,2,4,4,7,8,9,5,9,8,0,5,0,3,5,5,2,6,8,3,4,1,4,7,1,7,2,7,5,8,8,7,2,2,3,9,2,2,7,3,2,9,0,2,3,6,9,7,2,8,0,8,1,6,5,2,3,0,2,0,0,0,9,2,2,2,3,6,6,0,9,1,0,0,3,5,8,3,2,0,3,5,1,4,1,6,8,7,6,0,9,8,0,1,0,4,5,6,0,2,8,2,5,0,2,8,5,2,3,0,2,6,7,3,0,0,2,1,9,0,1,9,9,2,0,1,6,7,7,9,9,6,1,4,8,5,5,6,7,0,6,1,7,3,5,9,3,9,0,5,9,2,4,8,6,6,2,2,3,9,3,5,7,4,1,6,9,8,2,6,9,0,0,8,5,7,7,0,6,0,5,7,4,9,6,0,7,8,4,3,9,8,8,7,4,1,5,6,0,9,4,1,9,4,9,4,1,8,6,7,8,2,5,2,3,3,4,3,3,1,6,4,1,6,1,5,7,8,1,9,7,6,0,8,0,1,4,4,0,1,1,8,3,8,3,8,3,9,1,6,0,7,1,3,3,4,9,3,5,2,4,2,0,7,3,3,8,7,7,8,8,0,9,3,1,2,2,4,3,3,3,6,1,6,9,6,2,0,1,7,5,6,2,5,3,5,0,3,2,7,2,3,0,3,6,1,7,8,7,0,4,0,6,7,6,6,3,9,8,5,8,3,3,0,9,6,7,1,9,2,1,3,5,1,6,3,4,3,4,1,6,8,4,2,5]
    s = Solution()
    print(s.superPow5(a, b))


