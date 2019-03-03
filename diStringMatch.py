class Solution:
    def diStringMatch(self, S: str):
        if not S:
            return ""
        tem = [0]
        for each in S:
            if each == 'I':
                tem += [tem[-1] + 1]
            else:
                tem += [tem[-1] - 1]
        print(tem)
        res = [-1 for _ in range(len(S)+1)]

        max_index = tem.index(max(tem))
        res[max_index] = len(S)

        print(res)


S = "IDID"

s = Solution()
print(s.diStringMatch(S))