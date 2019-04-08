class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        def return_num(n):
            word_hash = {}
            word_index_list = []
            for index, num in enumerate(n):
                if num in word_hash:
                    word_index_list.append(word_hash[num])
                else:
                    word_hash[num] = index
                    word_index_list.append(index)
            return word_index_list


        if not pattern:
            return []
        if not words:
            return []

        pattern_str = return_num(pattern)
        res = []
        for each_words in words:
            each_words_num = return_num(each_words)
            if each_words_num == pattern_str:
                res.append(each_words)
        return res



words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
s = Solution()
print(s.findAndReplacePattern(words, pattern))