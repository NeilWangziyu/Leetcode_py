class Solution:
    def partitionLabels(self, S: str):
        if not S:
            return []
        res = []
        length = len(S)
        point_lo = 0
        while(True):
            checkedChar = set()
            print(S[point_lo])
            if S[point_lo] not in checkedChar:
                checkedChar.add(S[point_lo])
                index_a = point_lo
                for i in range(index_a, length):
                    if S[i] == S[point_lo]:
                        index_a = i

                res.append(index_a - point_lo + 1)
                point_lo = index_a + 1

            if point_lo == length:
                break

        print(checkedChar)
        return res








S = "ababcbacadefegdehijhklij"
s = Solution()
print(s.partitionLabels(S))