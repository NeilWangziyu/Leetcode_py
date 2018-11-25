class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)
        else:
            whole = numerator // denominator
            # whole 是整数
            left = numerator % denominator
            dict_nown = {}
            left_num = []
            while(left != 0 and (whole not in dict_nown)):
                print(whole)
                print(left)
                print(dict_nown)
                left = left * 10
                whole = left // denominator
                left = left % denominator
                left_num.append(left)
                dict_nown[whole] = True



            if left == 0:
                return str(whole) + "." + "".join(left_num)
            else:
                return str(whole) + "." + "(" + "".join(left_num) + ")"





s = Solution()
print(s.fractionToDecimal(numerator = 2, denominator = 3))

