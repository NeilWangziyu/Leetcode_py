from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        hash_set = {}
        cout = 0
        for each in dominoes:
            each.sort()
            each_str = "".join(map(str,each))
            if each_str not in hash_set:
                hash_set[each_str] = 1
            else:
                hash_set[each_str] += 1
        for each in hash_set.keys():
            if hash_set[each] > 1:
                cout += hash_set[each]*(hash_set[each]-1)/2
        return int(cout)


if __name__ == "__main__":
    s = Solution()
    print(s.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))