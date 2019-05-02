class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        n,m = 0,0
        res = []
        for index, each in enumerate(S):
            if each == '(':
                n += 1
            else:
                m += 1
            if n == m:
                res.append(S[index - n - m +2:index])
                n ,m = 0, 0
        return "".join(res)

    def removeOuterParentheses2(self, S: str) -> str:
        count = 0
        res = ""
        for i in S:
            if i == "(":
                count += 1
                if count > 1:
                    res += i
            else:
                count -= 1
                if count > 0:
                    res += i

        return res


S = "(()())(())(()(()))"
s = Solution()
print(s.removeOuterParentheses(S))
