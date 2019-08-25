from typing import List
from collections import Counter
import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries_list = []
        words_list = []
        for each in queries:
            each_counter = Counter(each)
            key_res = sorted(each_counter)
            queries_list.append(each_counter[key_res[0]])
        # print(queries_list)
        for each_word in words:
            each_Word_counter = Counter(each_word)
            word_key_res = sorted(each_Word_counter)
            words_list.append(each_Word_counter[word_key_res[0]])
        words_list.sort(reverse=False)
        # print(words_list)

        res = []
        for each in queries_list:
            index = bisect.bisect_right(words_list, each)
            # print(each, index)
            res.append(len(words_list) - index)
        return res





s = Solution()
queries = ["cbd"]
words = ["zaaaz"]
print(s.numSmallerByFrequency(queries, words))

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(s.numSmallerByFrequency(queries, words))

