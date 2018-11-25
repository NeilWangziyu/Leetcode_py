class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        stack_list = []
        while(tokens):
            t = tokens.pop(0)
            print(t)
            if t.lstrip('-').isdigit():
                # 注意isdigit不可以对负数用
                stack_list.append(int(t))
            else:
                print(stack_list)
                a1 = (stack_list.pop(-1))
                a2 = (stack_list.pop(-1))
                if t == "+":
                    ans= a2 + a1
                elif t == "-":
                    ans = a2 - a1
                elif t == "*":
                    ans = a2 * a1
                else:
                    ans = int(a2 / a1)

                stack_list.append((ans))
        return stack_list[0]





token = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(token))