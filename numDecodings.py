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
        :param s:
        :return:
        """





s = Solution()
print(s.numDecodings("30"))
print("-----------")
print(s.numDecodings2("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))