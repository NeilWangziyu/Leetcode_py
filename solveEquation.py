class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        if not equation:
            return "Infinite solutions"

        left = True
        stack = []
        x_num = 0
        other_num = 0


        plus = True

        for i in range(len(equation)):
            if equation[i] == '=':

                if not stack:
                    left = False
                    plus = False
                    continue
                else:
                    if plus == True:
                        other_num += int("".join(stack))
                    else:
                        other_num -= int("".join(stack))

                    left = False
                    plus = False
                    stack = []
                    continue




            if left == True:
                if equation[i] == 'x':
                    if not stack:
                        if plus == True:
                            x_num += 1
                        else:
                            x_num -= 1

                    else:
                        if plus == True:
                            x_num += int("".join(stack))
                        else:
                            x_num -= int("".join(stack))


                    stack = []
                    plus = True

                elif equation[i] == '+':
                    if stack:
                        if plus == True:
                            other_num += int("".join(stack))
                        else:
                            other_num -= int("".join(stack))

                    plus = True
                    stack = []

                elif equation[i] == '-':
                    if stack:

                        if plus == True:
                            other_num += int("".join(stack))
                        else:
                            other_num -= int("".join(stack))

                    plus = False
                    stack = []

                else:
                    stack.append(equation[i])

            else:
                # left == False
                if equation[i] == 'x':
                    if not stack:
                        if plus == True:
                            x_num += 1
                        else:
                            x_num -= 1

                    else:
                        if plus == True:
                            x_num += int("".join(stack))
                        else:
                            x_num -= int("".join(stack))

                    stack = []
                    plus = False
                elif equation[i] == '+':
                    if stack:

                        if plus == True:
                            other_num += int("".join(stack))
                        else:
                            other_num -= int("".join(stack))

                    plus = False
                    stack = []

                elif equation[i] == '-':
                    if stack:

                        if plus == True:
                            other_num += int("".join(stack))
                        else:
                            other_num -= int("".join(stack))

                    plus = True
                    stack = []

                else:
                    stack.append(equation[i])


        if len(stack) > 0:

            if plus == True:
                other_num += int("".join(stack))
            else:
                other_num -= int("".join(stack))

        print(x_num, other_num)

        if x_num == 0 and other_num == 0:
            return "Infinite solutions"
        if x_num == 0 and other_num != 0:
            return "No solution"
        else:
            res = int(-other_num / x_num)
            return "x="+str(res)


s = Solution()
print(s.solveEquation(equation="x+5-3+x=6+x-2"))


print(s.solveEquation(equation="x=x"))

print(s.solveEquation(equation="2x=x"))

print(s.solveEquation(equation="2x+3x-6x=x+2"))

print(s.solveEquation(equation="x=x+2"))

print(s.solveEquation(equation="-x=1"))

print(s.solveEquation(equation="1+1=x"))