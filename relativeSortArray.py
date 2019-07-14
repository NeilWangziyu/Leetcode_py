from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1:
            return arr1
        if not arr2:
            return arr1
        from collections import Counter
        arr1counter = Counter(arr1)

        res = []
        for each in arr2:
            if each in arr1counter:
                res += [each] * arr1counter[each]
                arr1counter.pop(each, None)
        if arr1counter:
            for each in sorted(arr1counter.keys()):
                res += [each] * arr1counter[each]
        return res
