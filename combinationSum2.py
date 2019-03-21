class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        res = []

        def DFS(index, length, check_list, K):
            if K == 0:
                if check_list not in res:
                    res.append(check_list)
                    return
            if index >= length:
                return

            for i in range(index, length):
                if K - candidates[i] >= 0:
                    DFS(i + 1, length, check_list + [candidates[i]], K - candidates[i])

        DFS(0, len(candidates), [], target)

        return res


    def combinationSum3(self, candidates, target):
        res = []
        candidates.sort()

        def find(candidates, target, l):
            if target in candidates:
                res.append(l + [target])
            if target > candidates[0]:
                for i in range(len(candidates) - 1):
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    find(candidates[i + 1:], target - candidates[i], l + [candidates[i]])

        find(candidates, target, [])
        return res







candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))
print(s.combinationSum3(candidates, target))