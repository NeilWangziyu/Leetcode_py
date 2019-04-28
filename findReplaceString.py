class Solution:
    def findReplaceString(self, S: str, indexes, sources, targets) -> str:
        if not str:
            return ""
        if not indexes:
            return S
        index_target = zip(indexes, sources, targets)
        index_target = sorted(index_target, key=lambda x:x[0], reverse=True)
        S_list = list(S)

        for each in index_target:
            # print(each)
            # print(S_list[each[0]:each[0]+len(each[1])])
            if S_list[each[0]:each[0]+len(each[1])] == list(each[1]):
                S_list[each[0]:each[0]+len(each[1])] = each[2]
        # print(S_list)
        return "".join(S_list)

    def findReplaceString2(self, S: str, indexes, sources, targets) -> str:

        for id, sc, tgt in sorted(zip(indexes, sources, targets), reverse=True):
            if S[id:id + len(sc)] == sc:
                S = S[:id] + tgt + S[id + len(sc):]
        return S


S = "abcdre"
indexes = [0, 2]
sources = ["ab", "ec"]
targets = ["eee", "ffff"]
s = Solution()
print(s.findReplaceString(S, indexes, sources, targets))
