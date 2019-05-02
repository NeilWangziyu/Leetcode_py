# https://leetcode-cn.com/problems/regular-expression-matching/
# 正则表达式匹配
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



# -----------------
# https://leetcode-cn.com/problems/regular-expression-matching/
# 实际上这道题比较粗暴，没有正则那题好
class Solution2:
    def isMatch(self, s, p):
        i, j = 0, 0  # 下个要匹配s,p的索引
        star = -1  # p中星号的最后的一个索引
        while i < len(s):
            if j >= len(p) or (p[j] not in {"*", "?"} and s[i] != p[j]):
                if star == -1:  # 没有星号 无法扩展
                    return False
                j = star + 1  # 有星号,于是模式p移动一位
                star_i += 1  # 使用星号匹配一位字符串,i移动一位
                i = star_i
            elif p[j] == "*":  # 记录下星号的索引,暂时不用,j移动一位
                star = j
                star_i = i  # star_i 是s中和*号匹配的第一个字符串的索引
                j += 1
            else:
                i += 1
                j += 1
        while j < len(p):  # 匹配完成后,p中还有剩余,检查是否有除了星号
            if p[j] != "*":
                return False
            j += 1
        return True


    def isMatch2(self, s, p):
        i, j = 0, 0
        star = -1
        while(i < len(s)):
            if j >= len(p) or (p[j] not in {"*", "?"} and s[i] != p[j]):
                if star == -1:
                    return False
                j = star + 1
                star_i += 1
                i = star_i
            elif p[j] == "*":
                star = j
                star_i = i
                j += 1
            else:
                i += 1
                j += 1
        while(j < len(p)):
            if p[j] != '*':
                return False
            j += 1
        return True

    def isMatch3(self, s, p) -> bool:
        s_len = len(s)
        p_len = len(p)
        i, j, star, i_index = 0, 0, -1, 0
        while i < s_len:
            if j < p_len and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                i_index = i
                j += 1
            elif star != -1:
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False
        while j < p_len and p[j] == '*':
            j += 1
        return j == p_len

if __name__ == "__main__":


    str = "aa"
    p = "a*"


    sp = Solution()
    print(sp.isMatch(str, p))
    print(sp.isMatch2(str, p))
    print(sp.isMatch3(str, p))