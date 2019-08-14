from typing import List
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 超时
        res = []
        for each in A:
            each_set = Counter(list(each))
            is_true = True
            for each_b_str in B:
                each_b_counter = Counter(list(each_b_str))
                for each_key in each_b_counter.keys():
                    if each_key not in each_set or each_b_counter[each_key] > each_set[each_key]:
                        is_true = False
                        break

            if is_true:
                res.append(each)
        return res

    def wordSubsets2(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        list_alpha = [0 for _ in range(26)]
        for each in B:
            counterB = Counter(each)
            for each_key in counterB.keys():
                index = ord(each_key) - ord("a")
                list_alpha[index] = max(list_alpha[index], counterB[each_key])

        for each in A:
            counterA = Counter(each)
            is_true = True
            for i in range(26):
                char1 = chr(i + ord("a"))
                if counterA[char1] < list_alpha[i]:
                    is_true = False
                    break
            if is_true:
                res.append(each)
        return res




s = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo", "oo"]
print(s.wordSubsets(A, B))
print(s.wordSubsets2(A, B))



