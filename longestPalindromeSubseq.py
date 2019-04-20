# https://leetcode-cn.com/problems/longest-palindromic-substring/
# 最长
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp[i][j]代表从i到j的最长的回文子串
        这个的点在于，中间是可以跳着的，只要找到两个一样的，就+2
        """
        if not s:
            return 0
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, length):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][length-1]

    def longestPalindromeSubseq2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:
            return n
        dp = [0] * n
        dp[n - 1] = 1
        for i in range(n - 1, -1, -1):
            tmp = dp[:]
            tmp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    tmp[j] = 2 + dp[j - 1]
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp = tmp[:]
        return dp[n - 1]


if __name__ == "__main__":
    sl = Solution()

    s = "bbbab"
    print(sl.longestPalindromeSubseq(s))

    s = "cbbd"
    print(sl.longestPalindromeSubseq(s))



