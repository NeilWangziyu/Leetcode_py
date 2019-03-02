class Solution:
    def checkValidString(self, s) -> bool:
        print(s)
        if not s:
            return True
        left = 0
        right = 0
        star = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == '*':
                star += 1
            else:
                if left > 0:
                    left -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False

        left = 0
        right = 0
        star = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            elif s[i] == '*':
                star += 1
            else:
                if right > 0:
                    right -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
        return True
    def checkValidString2(self, s) -> bool:
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(s):
            if s[i] == '(':
                a += 1
            elif s[i] == '*':
                b += 1
            elif s[i] == ')':
                if a > 0:
                    a -= 1
                elif b > 0:
                    b -= 1
                else:
                    return False
            if s[-i - 1] == ')':
                c += 1
            elif s[-i - 1] == '*':
                d += 1
            elif s[-i - 1] == '(':
                if c > 0:
                    c -= 1
                elif d > 0:
                    d -= 1
                else:
                    return False
        return True


str = "(*))"
s = Solution()
print(s.checkValidString(str))