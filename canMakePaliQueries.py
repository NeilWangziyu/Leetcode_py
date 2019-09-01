from typing import List
from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        if not s:
            return []
        if not queries:
            return []
        c_list = []
        tem_dict = {}
        c_list.append(tem_dict.copy())
        for i in range(len(s)):
            if s[i] not in tem_dict:
                tem_dict[s[i]] = 1
            else:
                tem_dict[s[i]] += 1
            c_list.append(tem_dict.copy())

        # c_list = [Counter(s[:k]) for k in range(len(s)+1)]
        # print(c_list)
        res = []
        for each in queries:
            str_input = s[each[0]:each[1]+1]
            each_left_dict = c_list[each[1]+1].copy()
            for each_key in c_list[each[0]]:
                each_left_dict[each_key] -= c_list[each[0]][each_key]

            if len(str_input) % 2 == 1:
#                 one char can be left
                c = 0
                for each_key in each_left_dict.keys():
                    if each_left_dict[each_key] % 2 == 1:
                        c += 1
                if c - 2*each[2] > 1:
                    res.append(False)
                else:
                    res.append(True)

            else:
#                 all must be even
                c = 0
                for each_key in each_left_dict.keys():
                    if each_left_dict[each_key] % 2 == 1:
                        c += 1
                if c - 2*each[2] > 0:
                    res.append(False)
                else:
                    res.append(True)
        return res



s = Solution()
print(s.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
