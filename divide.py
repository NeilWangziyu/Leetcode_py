class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        zfill第一次见
        """
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            f = -1
        else:
            f = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        a = list(bin(dividend)[2:])
        b = list(bin(divisor)[2:])
        length = len(b)
        ans = []
        nb = divisor
        print(a, b)
        for i in range(length, len(a) + 1):
            t = a[:i]
            na = int("".join(t), 2)
            print(t, na)
            if na >= nb:
                tem = list(bin(na - nb)[2:].zfill(len(t)))
                a[:i] = tem
                ans.append(1)
            else:
                ans.append(0)
            print(ans)
        if len(ans) == 0:
            return 0
        ret = int(''.join([str(c) for c in ans]), 2)

        if f == -1:
            ret = ~ret + 1

        Min_val = -2 ** 31
        Max_val = 2 ** 31 - 1
        if ret > Max_val or ret < Min_val:
            return Max_val
        return ret




    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 首先这一句就很python，postive 为true是符号相同
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        # 检查dividend是否大于divisor
        # 如果还小于则进行小精度的逼近dividend
        while dividend >= divisor:
            temp, i = divisor, 1
            # 增大逼近dividend的步伐
            # i不断增加， temp不断减少
            while dividend >= temp:
                # 经过上一句的判断，所以dividend还大于0
                dividend -= temp
                # 商要加对应的i
                res += i
                # 倍数相应的要增加
                i = i << 1
                # 目前的值也要不断的增加
                temp = temp << 1
        # 判定正负号
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


s = Solution()
print(s.divide(dividend=20, divisor=3))