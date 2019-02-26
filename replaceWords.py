class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict_root = set(dict)
        s_word = sentence.split()
        res = []
        for each in s_word:
            i = 1
            while(i<len(each)):
                if each[:i] in dict_root:
                    break
                i += 1
            res.append(each[:i])

        return " ".join(res)





dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

s = Solution()
print(s.replaceWords(dict, sentence))