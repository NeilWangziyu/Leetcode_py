class Solution:
    count = 0
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 26:
                if s != '10' and s != '20':
                    return 2
                else:
                    return 1
            else:
                if s[1] != "0" and s[0] != "0" :
                    return 1
                else:
                    return 0

        res = []
        for i in range(len(s)):
            res.append(0)

        if s[-1]==0:
            res[-1] = 0
        else:
            res[-1] = 1

        for i in range(-1, -len(s)):
            pass

        if int(s[:2]) > 26:
            return self.numDecodings(s[1:])
        else:
            if s[:2] == '10' or s[:2] == '20':
                return self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])



    def numDecodings2(self, s):
        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 26:
                if s != '10' and s != '20':
                    return 2
                else:
                    return 1
            else:
                if s[1] != "0" and s[0] != "0" :
                    return 1
                else:
                    return 0


        def DFS(start, end):
            # print(s[start:end])
            if end >= len(s):
                if int(s[start:end])>0 and int(s[start:end])<27:
                    if s[start:end][0] != "0":
                        self.count += 1
            else:
                if end - start <=2:
                    DFS(start, end+1)

                if int(s[start:end])>0 and int(s[start:end])<27:
                    if s[start:end][0] != "0":
                        DFS(end,end+1)
                        return
                else:
                    return

        DFS(0, 1)
        return self.count

    def numDecodings3(self, s):
        """
        需要动态规划进行计算
        t[i] =  t[i-1] + t[i-2]  || t[i-1] || t[i-2]
        :param s:
        :return:
        """
        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 26:
                if s != '10' and s != '20':
                    return 2
                else:
                    return 1
            else:
                if s[1] != "0" and s[0] != "0" :
                    return 1
                else:
                    return 0
        dp = [0 for _ in range(len(s)+1)]

        dp[1] = self.numDecodings(s[:1])
        dp[2] = self.numDecodings(s[:2])
        # print(dp)
        for i in range(3, len(s)+1):
            print(s[i-1:i])
            if int(s[i-1:i])!=0:
                if int(s[i-2:i])>0 and int(s[i-2:i])<27 and int(s[i-2:i-1])!=0:
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if int(s[i-2:i])>0 and int(s[i-2:i])<27:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0
        print(dp)
        return dp[-1]



    def numDecodings4(self, s):
        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i != 1 and int(s[i - 2:i]) > 9 and int(s[i - 2:i]) < 27:
                dp[i] += dp[i - 2]
        return dp[len(s)]







s = Solution()
print(s.numDecodings("301"))
print("-----------")
print(s.numDecodings3("301"))
# print(s.numDecodings3("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))