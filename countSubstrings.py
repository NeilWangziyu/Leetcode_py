class Solution:
    def countSubstrings(self, s) -> int:
        if not s:
            return 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        res = len(s)
        for i in range(len(s)-2, -1, -1):
            # 从倒数第二个开始
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
            for j in range(i+2, len(s)):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1
        return res
#     time O^2, space: O^2

    def countSubstrings2(self, s) -> int:
        if not s:
            return 0
        res = 1
        length = len(s)
        for i in range(1, length):
            left = i
            right = i
            while(left >= 0 and right < length and s[left] == s[right]):
                res += 1
                left -= 1
                right += 1
            left = i - 1
            right = i
            while (left >= 0 and right < length and s[left] == s[right]):
                res += 1
                left -= 1
                right += 1
        return res
#     time O, space: 1

    def countSubstrings3(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = j = res = 0
        while i < n:
            while j < n and s[i] == s[j]:
                j += 1
            res += (1 + j - i) * (j - i) // 2
            l, r = i - 1, j
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            i = j
        return res


str = "aaa"
s = Solution()
print(s.countSubstrings2(str))