# https://leetcode-cn.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 最长公共子序列问题
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        len_word1 = len(word1)
        len_word2 = len(word2)
        dp = [[float('inf') for _ in range(len_word2+1)] for _ in range(len_word1+1)]
        dp[0][0] = 0
        for i in range(len_word1+1):
            dp[i][0] = i
        for j in range(len_word2+1):
            dp[0][j] = j

        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[len_word1][len_word2]


if __name__ == "__main__":
    s = Solution()

    word1 = "a"
    word2 = "b"

    print(s.minDistance(word1, word2))

    word1 = "sea"
    word2 = "eat"

    print(s.minDistance(word1, word2))