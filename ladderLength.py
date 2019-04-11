class Solution:
    # 每次转换只能改变一个字母。
    # 转换过程中的中间单词必须是字典中的单词。
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        # BFS
        """
        







beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))