class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def MatchCore(s, p, s_check, p_check, length_s, length_p):
            if s_check >= length_s and p_check >= length_p:
                return True
            if s_check != length_s and p_check >= length_p:
                return False
            if p[p_check + 1] == '*':
                #下一个字符是*
                if p[p_check] == s[s_check] or (p[p_check] == '.' and s_check != length_s):
                    return MatchCore(s, p, s_check+1, p_check+2, length_s, length_p) or MatchCore(s, p, s_check+1, p_check, length_s, length_p) or \
                           MatchCore(s, p, s_check, p_check + 2, length_s, length_p)
                else:
                    return MatchCore(s, p, s_check, p_check + 2, length_s, length_p)
            if p[p_check] == s[s_check] or (p[p_check] == '.' and s_check!=length_s):
                return MatchCore(s, p, s_check+1, p_check+1, length_s, length_p)
            return False

        s = s + '#'
        p = p + '#'
        length_s = len(s) - 1
        length_p = len(p) - 1
        s_check = 0
        p_check = 0
        return MatchCore(s, p, s_check, p_check, length_s, length_p)

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            for j in range(0, len(s) + 1):
                if p[i - 1] == '.':
                    if i >= 2 and p[i - 2] == '*' and j == 0:
                        dp[i][j] = False
                    if j >= 1 and dp[i - 1][j - 1] is True:
                        dp[i][j] = True
                elif p[i - 1] == '*':
                    if dp[i - 1][j] is True:
                        dp[i][j] = True
                    elif dp[i][j - 1] is True and p[i - 2] == '.':
                        dp[i][j] = True
                    elif dp[i - 2][j] is True:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] is True and (p[i - 2] == s[j - 1] or
                                                       p[i - 2] == '.'):
                        dp[i][j] = True
                elif j >= 1 and dp[i - 1][j - 1] is True and p[i - 1] == s[j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]

    def isMatch3(self, s, p):
        """
        note-----------------------
        '.'匹配任意字符，'*'只能匹配任意多个前面的字符

        do-------------------------
        use 2 pointers
        Created on Fri Nov 17 2018
        """
        if s == p:
            return True
        if len(p) > 1 and p[1] == '*':
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        elif s and p and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return False


if __name__ == "__main__":


    str = "aa"
    p = "a*"


    sp = Solution()
    print(sp.isMatch(str, p))
    print(sp.isMatch2(str, p))
    print(sp.isMatch3(str, p))