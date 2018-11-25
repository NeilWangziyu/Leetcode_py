class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dict_word = {}
        for each in words:
            dict_word[each] = 1
            for i in range(1, len(each)):
                if each[:i] not in dict_word:
                    dict_word[each[:i]] = 0

        print(dict_word)
        max_length = 0
        max_word = None

        words.sort()
        for each in words:
            if len(each) > max_length:
                flag = True
                for i in range(1, len(each)):
                    if dict_word[each[:i]] == 0:
                        flag = False
                        break

                if flag == True:
                    max_length = len(each)
                    max_word = each
        return max_word

        #  another solution
        # wordSet = set(words)
        #
        # result = ''
        # for word in wordSet:
        #     if (len(word) > len(result) or len(word) == len(result) and word < result):
        #
        #         if all(word[:k] in wordSet for k in range(1, len(word))):
        #             result = word
        #
        # return result


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

s = Solution()
print(s.longestWord(words))
