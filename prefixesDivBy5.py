class Solution:
    def prefixesDivBy5(self, A):
        if not A:
            return []
        res = ""
        res_list = []
        for each in A:
            res += str(each)
            num = int(res, 2)
            if num % 5 == 0:
                res_list.append(True)
            else:
                res_list.append(False)
        return res_list
