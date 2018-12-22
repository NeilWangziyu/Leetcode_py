class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [-1 for _ in range(len(S))]
        before_C = -1
        for index, num in enumerate(S):
            if num == C:
                res[index] = 0
                before_C = index
            else:
                if before_C == -1:
                    continue
                else:
                    res[index] = index - before_C
        # print(res)
        res = res[::-1]
        S = S[::-1]
        before_C = -1
        for index, num in enumerate(S):
            if num == C:
                if num == C:
                    before_C = index
            else:
                if before_C == -1:
                    continue
                else:
                    if res[index] == -1:
                        res[index] = index - before_C
                    elif index - before_C < res[index]:
                        res[index] = index - before_C
                    else:
                        continue
        res = res[::-1]
        return res


S = "loveleetcode"
C = 'e'
s = Solution()
print(s.shortestToChar(S, C))