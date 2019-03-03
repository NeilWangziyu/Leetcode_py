class Solution:
    def commonChars(self, A):
        from collections import Counter
        if not A:
            return []
        res = Counter(A[0])
        if len(A)==1:
            res_list = []
            for each in res.keys():
                res_list += [each] * res[each]
                return res_list

        for each_word in A[1:]:
            check_list = res.keys()
            tem_c = Counter(each_word)
            next_res = {}
            for each in check_list:
                if each not in tem_c:
                    pass
                else:
                    next_res[each] = min(tem_c[each], res[each])
            res = next_res
        res_list = []
        for each_c in res.keys():
            res_list += [each_c] * res[each_c]
        return res_list


A =["bella","label","roller"]
s = Solution()
print(s.commonChars(A))
