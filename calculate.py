class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        #
        # s = list(s)
        # list_a = []
        #
        # input_num = ""
        # while(s):
        #     num = s.pop(0)
        #     if num.isdigit():
        #         input_num = input_num + num
        #     elif num != " ":
        #         list_a.append(int(input_num))
        #         input_num = ""
        #         list_a.append(num)
        #     else:
        #         # 空格
        #         pass
        # list_a.append(int(input_num))
        # # print(list_a)
        # next_level = []
        # while(list_a):
        #     print(list_a)
        #     num = list_a.pop(0)
        #     if isinstance(num, int):
        #         next_level.append(num)
        #     elif num == "+":
        #         next_level.append(list_a.pop(0))
        #     elif num == "-":
        #         next_level.append(-list_a.pop(0))
        #     elif num == "*":
        #         first = next_level.pop()
        #         next = list_a.pop(0)
        #         next_level.append(first*next)
        #     elif num == '/':
        #         first = next_level.pop()
        #         next = list_a.pop(0)
        #         if first >= 0:
        #             next_level.append(first // next)
        #         else:
        #             next_level.append(-(abs(first) // next))
        # print(next_level)
        # res = sum(next_level)
        #
        #
        # return res

        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)





s = Solution()
print(s.calculate("14-3/2"))