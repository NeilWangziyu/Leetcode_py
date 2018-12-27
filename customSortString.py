class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dict_T = {}
        for index, each in enumerate(T):
            if each not in dict_T:
                dict_T[each] = 1
            else:
                dict_T[each] += 1

        res = []
        for each in S:
            if each in dict_T:
                res.append(each * dict_T[each])
                dict_T.pop(each)

        left = list(dict_T.keys())
        for each in left:
            res.append(each * dict_T[each])
        return "".join(res)




S = "cba"
T = "abbcd"

s = Solution()
print(s.customSortString(S, T))

