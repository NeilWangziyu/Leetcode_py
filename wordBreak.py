class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        out of time
        """
        def DFS(start, index, tem):
            if index == len(s):
                if index == start:
                    res.append(tem)
                    return
                else:
                    return

            if s[start:index+1] in DictOfWord:
                DFS(index+1, index+1, tem+[s[start:index+1]])

            DFS(start, index+1, tem)

        DictOfWord = {}
        for each in wordDict:
            DictOfWord[each] = True
        # print(DictOfWord)
        res = []
        DFS(0, 0, [])
        res_str = []
        for each in res:
            res_str.append(" ".join(each))
        return res_str


    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def DFS(str):
            if str == "":
                return True, []
            res = []
            for each in DictOfWord.keys():
                if each == str[:len(each)]:
                    final, next = DFS(str[len(each):])
                    if final == True:
                        res.append([each])
                    else:
                        if next != []:
                            for each_sub in next:
                                res.append([each] + each_sub)
            if res == []:
                return False, res
            else:
                return False, res

        DictOfWord = {}
        for each in wordDict:
            DictOfWord[each] = True
        found, return_list = DFS(s)
        return_l = []
        for each_str in return_list:
            return_l.append(" ".join(each_str))
        return return_l

    def wordBreak3(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: List[str]
            """
            Solution.res = []
            self.dfs(s, wordDict, '')
            return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
                # 如果s已经切完，则加入最后结果集
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    # print(stringlist + ' ' + s[:i])
                    self.dfs(s[i:], wordDict, stringlist + ' ' + s[:i])

    def check(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
            # 这里循环是len(s)，使得该check函数变成了只要有单词在里面就验证成功，和wordbreak有所不同！
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[len(s)]

    # ----------方法四
    def backtrack(self, s, hashmap): # 使用回溯法构造答案
        n = len(s)
        temp = []
        for i in hashmap[n]:
            if i == 0:
                temp.append(s)
            else:
                for string in self.backtrack(s[:i], hashmap):
                    temp.append(string + ' ' + s[i:])
        return temp

    def wordBreak4(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 动态规划 + hashmap + 回溯
        # 记录被拆分的位置，然后使用回溯法输出结果
        wordlen = {len(word) for word in wordDict}
        words = set(wordDict)
        n = len(s)
        hashmap = {i:[] for i in range(1, n+1)} # 记录前缀字符串s[:i)被拆分的位置，这里i是前缀字符串的长度
        for length in wordlen:
            if s[:length] in words:
                hashmap[length].append(0)
        for i in range(1, n+1): # i还是指前缀字符串的长度
            for length in wordlen:
                if i > length and s[i-length:i] in words and hashmap[i-length]:
                    hashmap[i].append(i-length)
        if not hashmap[n]:
            return []
        else:
            return self.backtrack(s, hashmap)





s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

t = Solution()
# print(t.wordBreak(s, wordDict))
print(t.wordBreak4(s, wordDict))
