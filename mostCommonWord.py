class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        # paragraph_after = filter(str.isalpha, paragraph)
        # print(list(paragraph_after))
        #
        # paragraph_list = paragraph.split(" ")
        # print(paragraph_list)

        import re
        paragraph_list_2 = re.split("\s|\.|!|\?|\'|,|;", paragraph)
        print([each for each in paragraph_list_2 if each !=""])
        list_p = [each for each in paragraph_list_2 if each !=""]
        dict_list = {}
        ban_list = {}

        for each in banned:
            ban_list[each] = True

        for each in list_p:
            if each not in ban_list:
                if each not in dict_list:
                    dict_list[each] = 1
                else:
                    dict_list[each] += 1
        print(max(dict_list, key=dict_list.get))

        return max(dict_list, key=dict_list.get)




paragraph = "Bob hit a ball, the hit BALL flew far after it was hit. tomorrow!, he said'I like it'."
banned = ["hit"]
s = Solution()
print(s.mostCommonWord(paragraph, banned))