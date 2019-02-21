class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        if not S:
            return 0
        stack = []
        for each in S:
            if not stack:
                stack.append(each)
            else:
                if each == ')':
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        stack.append(each)
                else:
                    stack.append(each)
        print(stack)
        return len(stack)



S = "()"
s = Solution()
print(s.minAddToMakeValid(S))