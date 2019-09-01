from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        hash_dict = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
        for each_word in words:
            word_set = set(each_word)
            for each_key in hash_dict.keys():
                if each_key in word_set:
                    hash_dict[each_key].append(word_set)

        res = []
        for puzzle in puzzles:
            if not puzzle:
                res.append(0)
            else:
                check_list = hash_dict[puzzle[0]]
                # print(check_list)
                if not check_list:
                    res.append(0)
                else:
                    c = 0
                    puzzle_set = set(puzzle)
                    # print(puzzle_set)
                    for each_possible_word_set in check_list:
                        if each_possible_word_set.issubset(puzzle_set):
                            c += 1
                    res.append(c)
        return res





s = Solution()
print(s.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))