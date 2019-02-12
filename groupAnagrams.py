class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        dict_base = {}

        for each in strs:
            each_r = "".join(sorted(list(each)))
            if each_r not in dict_base:
                dict_base[each_r] = [each]
            else:
                dict_base[each_r].append(each)


        res = []
        for each in dict_base.keys():
            res.append(dict_base[each])

        return res




strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))