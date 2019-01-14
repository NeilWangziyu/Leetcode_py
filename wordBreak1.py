class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False
        wordDict_Set = set(wordDict)
        check_list = [False for _ in range(len(s)+1)]
        check_list[0] = True
        for i in range(1, len(s)+1):
            for j in range(len(wordDict)):
                if i >= len(wordDict[j]):
                    if s[i-len(wordDict[j]):i] in wordDict_Set and check_list[i-len(wordDict[j])]== True:
                        print(s[i-len(wordDict[j]): i])
                        check_list[i] = True

        print(check_list)
        return check_list[-1]





string = "applepenapple"
wordDict = ["apple", "pen"]
s = Solution()
print(s.wordBreak(string, wordDict))