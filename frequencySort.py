class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # import sorted 和 sort的区别，sort只能应用在list上面，而sorted可以用在
        # 所有的可迭代对象上面
        dict_s = {}
        for each in s:
            if each not in dict_s:
                dict_s[each] = 1
            else:
                dict_s[each] += 1
        print(dict_s.keys())
        # for key, each in enumerate(dict_s):
        #     print(key, each, dict_s[each])

        t = sorted(dict_s.keys(), key=lambda x:dict_s[x], reverse=True)
        print(t)
        res = ""
        for each in t:
            res += each * dict_s[each]
        return res

s = Solution()
print(s.frequencySort("bcccaaa"))
