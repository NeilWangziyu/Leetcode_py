from typing import List
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_c = Counter(list(chars))
        res = 0
        for each in words:
            each_c = Counter(list(each))
            check = True
            for each_key in each_c.keys():
                if each_key not in chars_c:
                    check = False
                    break
                else:
                    if each_c[each_key] > chars_c[each_key]:
                        check = False
                        break
            if check:
                res += len(each)
        return res


s = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(s.countCharacters(words, chars))