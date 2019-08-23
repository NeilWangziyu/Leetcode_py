from typing import List
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_num = {}
        for each in nums:
            if each not in dict_num:
                dict_num[each] = 1
            else:
                dict_num[each] += 1
        print(dict_num.keys())
        print(dict_num)
        res = sorted(dict_num.keys(), key=lambda x:dict_num[x], reverse=True)
        print(res[:k])

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,2,2,2,3,4], k = 2))


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        c = Counter(words)
        res = sorted(sorted(c.keys()), key=lambda x:c[x], reverse=True)[:k]
        return res

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for s in words:
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1
        print(dic)
        print(dic.items())

        li = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        print(li)
        res = []
        for i in range(k):
            res.append(li[i][0])
        return res


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
s2 = Solution2()
print(s2.topKFrequent2(words, k))