class Solution:
    # https://leetcode-cn.com/problems/edit-distance/submissions/
    # 这题真的好题目
    # dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
    # 三种情况，替换，或者word1加一个，或者word2加一个

    def minDistance(self, word1: str, word2: str) -> int:
        """
        问题1：如果 word1[0..i-1] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要几步呢？
        答：先使用 k 步，把 word1[0..i-1] 变换到 word2[0..j-1]，消耗 k 步。再把 word1[i] 改成 word2[j]，就行了。如果 word1[i] == word2[j]，什么也不用做，一共消耗 k 步，否则需要修改，一共消耗 k + 1 步。

        问题2：如果 word1[0..i-1] 到 word2[0..j] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？
        答：先经过 k 步，把 word1[0..i-1] 变换到 word2[0..j]，消耗掉 k 步，再把 word1[i] 删除，这样，word1[0..i] 就完全变成了 word2[0..j] 了。一共 k + 1 步。

        问题3：如果 word1[0..i] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？
        答：先经过 k 步，把 word1[0..i] 变换成 word2[0..j-1]，消耗掉 k 步，接下来，再插入一个字符 word2[j], word1[0..i] 就完全变成了 word2[0..j] 了。

        从上面三个问题来看，word1[0..i] 变换成 word2[0..j] 主要有三种手段，用哪个消耗少，就用哪个。
        """

        len1 = len(word1)
        len2 = len(word2)

        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len2+1):
            dp[0][i] = i


        for i in range(1, len1+1):
            dp[i][0] = i

        # print(dp)

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    # 相等，直接替换
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
        return dp[-1][-1]



    def minDistance3(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        height, width = len(word1), len(word2)
        if height == 0:
            return width
        elif width == 0:
            return height

        ans = [[0] * width for _ in range(height)]
        if word1[0] != word2[0]:
            ans[0][0] = 1

        # 先处理上边界
        for w in range(1, width):
            if word2[w] == word1[0]:
                ans[0][w] = w
            else:
                ans[0][w] = ans[0][w - 1] + 1

        # 再处理左边界
        for h in range(1, height):
            if word2[0] == word1[h]:
                ans[h][0] = h
            else:
                ans[h][0] = ans[h - 1][0] + 1

        # 开始规划：如果word1
        for h in range(1, height):
            for w in range(1, width):
                if word1[h] == word2[w]:
                    ans[h][w] = ans[h - 1][w - 1]
                else:
                    ans[h][w] = min(ans[h - 1][w - 1], ans[h - 1][w], ans[h][w - 1]) + 1
        return ans[-1][-1]

    def minDistance2(self, word1: 'str', word2: 'str') -> 'int':
        result = [{} for _ in range(len(word1) + 1)]

        def getDistance(i, j):
            if i == 0: return j
            if j == 0: return i
            if j in result[i]: return result[i][j]

            if word1[i - 1] == word2[j - 1]:
                distance = getDistance(i - 1, j - 1)
            else:
                distance = min(getDistance(i - 1, j - 1),
                               getDistance(i - 1, j),
                               getDistance(i, j - 1)) + 1
            result[i][j] = distance
            return distance

        return getDistance(len(word1), len(word2))

    def minDistance4(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1) + 1, len(word2) + 1

        cur = [0] * n
        for i in range(n):
            cur[i] = i

        for i in range(1, m):
            temp = cur[0]
            cur[0] = i
            for j in range(1, n):
                pre = temp
                temp = cur[j]

                if word1[i - 1] == word2[j - 1]:
                    cur[j] = pre
                else:
                    cur[j] = min(pre, temp, cur[j - 1]) + 1
        return cur[-1]


word1 = "horse"
word2 = "ros"
s = Solution()
print(s.minDistance(word1, word2))