class Solution:
    def longestValidParentheses(self, s) -> int:
        # 对字符串遍历，进行括弧有效性验证，记录最大的有效长度。同样的方式，倒序再来一次，取最大值。时间复杂度 2*s.length
        if not s:
            return 0
        if len(s) == 1:
            return 0

        def check(string, start, end, flag):
            max_tem = 0
            sum = 0
            currLen = 0
            validLen = 0
            for i in range(start, end):
                if string[i] == flag:
                    sum += 1
                else:
                    sum -= 1
                currLen += 1
                if sum < 0:
                    max_tem = max(max_tem, validLen)
                    sum = 0
                    currLen = 0
                    validLen = 0
                elif sum == 0:
                    validLen = currLen
            return max(max_tem, validLen)

        return max(check(s, 0, len(s), '('), check(s[::-1], 0, len(s), ')'))

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        最佳方法
        """
        stack = []
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    res = max(res, i - start)
                    start = i + 1
                    continue
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - start + 1)
                    if stack:
                        res = max(res, i - stack[-1])
        return res


str = "()(()"
s = Solution()
print(s.longestValidParentheses(str))
print(s.longestValidParentheses2(str))