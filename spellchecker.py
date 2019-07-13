from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        raw_wordlist = set(wordlist)

        init_dict = {}
        for each in wordlist:
            tem = each.lower()
            if tem not in init_dict:
                init_dict[tem] = each

        # AEIOU
        AEIOU_dict = {}
        for each in wordlist:
            lower_each = each.lower()
            tem = ""
            for i in lower_each:
                if i in set('aeiou'):
                    tem += '.'
                else:
                    tem += i

            if tem not in AEIOU_dict:
                AEIOU_dict[tem] = each


        res = []
        for each in queries:
            if each in raw_wordlist:
                res.append(each)
            elif each.lower() in init_dict:
                res.append(init_dict[each.lower()])
            else:
                tem = ""
                lower_each = each.lower()
                tem = ""
                for i in lower_each:
                    if i in set('aeiou'):
                        tem += '.'
                    else:
                        tem += i
                if tem in AEIOU_dict:
                    res.append(AEIOU_dict[tem])
                else:
                    res.append("")

        return res



if __name__ == "__main__":
    s = Solution()

    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

    print(s.spellchecker(wordlist, queries))


