class Solution:
    def strStr(self, s, t):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        KMP算法
        """
        if not t:
            return 0
        if not s:
            return -1

        len_s = len(s)
        len_t = len(t)
        r = [0] * len_t
        r[0] = -1
        j = -1
        print(r)

        for i in range(1, len_t):
            while j >= 0 and t[i - 1] != t[j]:
                j = r[j]
            j += 1
            r[i] = j
        # 用r[j]来记录j减去自身与t[0,...,j-1]的差值

        j = 0
        # print(r)

        for i in range(len_s):
            while j >= 0 and s[i] != t[j]:
                j = r[j]
            j += 1
            if j == len_t:
                return i - len_t + 1
        return -1

    def strStr2(self,haystack, needle):
        return haystack.find(needle)

    def strStr3(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        # if m < n:
        #     return -1
        for i in range(m - n + 1):
            if haystack[i:n + i] == needle:
                return i
        return -1



haystack = "hello"
needle = "ll"
s = Solution()
print(s.strStr(haystack, needle))