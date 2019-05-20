class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        就是求最大公共字串，要求这些字串ascii值最大
        Let dp(i, j) be the answer for inputs s1[i:] and s2[j:].
        1.s1[i-1] == s2[j-1]，新增的两个字符相等的情况下，没有必要删除之前的结果，因此dp[i][j] = dp[i-1][j-1]
        2.s1[i-1] != s2[j-1]，取三者的最小值
        （1）保留s2串，删除s1串的字符，dp[i][j] = dp[i-1][j] + s1.charAt(i-1)
        （2）保留s1串，删除s2串的字符，dp[i][j] = dp[i][j-1] + s1.charAt(j-1)
        （3）删除s1、s2串的字符，dp[i][j] = dp[i-1][j-1] + s1.charAt(i-1) + s2.charAt(j-1)
        """
        DP = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            DP[i][0] = DP[i-1][0] + ord(s1[i-1])
        for i in range(1, len(s2)+1):
            DP[0][i] = DP[0][i-1] + ord(s2[i-1])
        # print(DP)
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    # print(i,j)
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(min(DP[i-1][j]+ord(s1[i-1]) , DP[i][j-1]+ ord(s2[j-1])), DP[i-1][j-1] + ord(s1[i-1])+ord(s2[j-1]))
        # print(DP)
        return DP[-1][-1]




s1 = "delete"
s2 = "leet"
s = Solution()
print(s.minimumDeleteSum(s1, s2))