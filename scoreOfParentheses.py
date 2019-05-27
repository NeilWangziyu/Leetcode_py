class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        Python eval() 函数

        """
        s = ''
        for i in range(len(S) - 1):
            if S[i] == '(':
                if S[i + 1] == "(":
                    s += "("
                else:
                    s += '1'
            else:
                if S[i + 1] == '(':
                    s += '+'
                else:
                    s += ')*2'
        return eval(s)


    def scoreOfParentheses2(self, S: str) -> int:
        deep, res = 0, 0
        for i in range(len(S)):
            if S[i] == "(":
                deep += 1
            else:
                deep -= 1
            if S[i] == ")" and S[i - 1] == "(":
                res += 2 ** deep
        return res


    def scoreOfParentheses3(self, S: str) -> int:
        lefts = rights = i = score = 0
        while i < len(S):
            if S[i] == '(':
                lefts += 1
            else:
                rights += 1
                if rights == lefts or S[i + 1] == '(':
                    score += 1 << (lefts - 1)
                    lefts -= rights
                    rights = 0
            i += 1
        return score

    def scoreOfParentheses4(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == "(":  # "("入栈
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:  # "()"情况
                    stack[-1] += 1
                else:  # "(A)" "AB" 情况
                    stack[-1] += 2 * last
        return stack.pop()


S = "(()(()))"
s = Solution()
print(s.scoreOfParentheses(S))
S = "(())"
print(s.scoreOfParentheses(S))

S = "()"
print(s.scoreOfParentheses(S))
S = "()()"
print(s.scoreOfParentheses(S))

