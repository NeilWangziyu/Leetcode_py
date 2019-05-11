class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        fractions..不能用
        """
        from fractions import Fraction

        if not expression:
            return "0/1"

        if expression[0] == '-':
            input_label = False
            first_need = False
        else:
            input_label = True
            first_need = True
        init = 0
        add_list = []
        seg_list = []
        for i in range(len(expression)):
            if expression[i] == '+':
                if first_need:
                    if input_label == True:
                        add_list.append(expression[init:i])
                    else:
                        seg_list.append(expression[init:i])
                    first_need = False
                else:

                    if input_label == True:
                        add_list.append(expression[init+1:i])
                    else:
                        seg_list.append(expression[init+1:i])

                init = i
                input_label = True

            elif expression[i] == '-':
                if first_need:
                    if input_label == True:
                        add_list.append(expression[init:i])
                    else:
                        seg_list.append(expression[init:i])
                    first_need = False
                else:
                    if input_label == True:
                        add_list.append(expression[init + 1:i])
                    else:
                        seg_list.append(expression[init + 1:i])

                init = i
                input_label = False

        if input_label == True:
            add_list.append(expression[init+1:])
        else:
            seg_list.append(expression[init+1:])


        # print(add_list)
        # print(seg_list)
        base = 0
        for each in add_list:
            if each != "":
                base += Fraction(each)
        for each in seg_list:
            if each != "":
                base -= Fraction(each)
        # print(base)
        # print(base.denominator)
        if base.denominator!= 1:

            return base
        else:
            return "{}/1".format(base)


    def fractionAddition2(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        def gcd(a, b):  # 最大公约数
            return b if a % b == 0 else gcd(b, a % b)

        def lcm(a, b):  # 最小公倍数
            return int(a * b / gcd(a, b))

        if expression.count('/') == 1: return expression

        expression = expression.replace('-', '+-')
        # 先替换，再拆分
        tmp = expression.split('+')

        tmp1 = []
        for x in tmp:
            if len(x):
                y = x.split('/')
                tmp1.append((int(y[0]), int(y[1])))
        fm, fz = 1, 0
        for x in tmp1:
            fm = lcm(fm, x[1])
        for x in tmp1:
            fz += x[0] * (fm // x[1])
        if fz == 0: return '0/1'
        gys = gcd(fm, abs(fz))
        return str(fz // gys) + '/' + str(fm // gys)


expression = "-1/2+1/2+1/3"
s = Solution()
print(s.fractionAddition(expression))
