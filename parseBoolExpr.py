class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = expression
        stack = []
        i = 0
        while(i < len(expression)):
            c = expression[i]

            if c == '(' or c == ',' or c == '!' or c == '&' or c == '|':
                stack.append(c)
                i += 1

            elif c == ')':
                if stack.pop() == 't':
                    ans = [True]
                else:
                    ans = [False]

                while(stack[-1]!= '('):
                    if stack[-1] == ',':
                        stack.pop()
                    else:
                        if stack.pop() == 't':
                            ans.append(True)
                        else:
                            ans.append(False)

                stack.pop()

                label = stack.pop()
                if label == '!' and len(ans) == 1:
                    # print(ans)
                    if ans[0] == True:
                        stack.append('f')
                    else:
                        stack.append('t')

                elif label == '&':
                    init = ans[0]
                    for each in ans[1:]:
                        init = init & each
                    if init == True:
                        stack.append('t')
                    else:
                        stack.append('f')

                elif label == '|':
                    init = ans[0]
                    for each in ans[1:]:
                        init = init | each
                    if init == True:
                        stack.append('t')
                    else:
                        stack.append('f')
                else:
                    init = ans[0]
                    if init == True:
                        stack.append('t')
                    else:
                        stack.append('f')
                i += 1
            else:
                stack.append(c)
                i += 1

            # print(stack)
        if stack[0] == 't':
            return True
        else:
            return False



s = Solution()



expression = "!(f)"
print(s.parseBoolExpr(expression))

expression = "&(t,f)"
print(s.parseBoolExpr(expression))


expression = "|(f,t)"
print(s.parseBoolExpr(expression))

expression = "|(&(t,f,t),!(t))"
print(s.parseBoolExpr(expression))