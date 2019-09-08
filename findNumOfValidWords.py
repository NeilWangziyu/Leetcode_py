from typing import List
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        hash_dict = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
        for each_word in words:
            word_set = set(each_word)
            for each_key in hash_dict.keys():
                if each_key in word_set:
                    hash_dict[each_key].append(word_set)
        # print(hash_dict)
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

# class Solution {
# public:
#     map<int,int> a;
#     vector<int> ans;
#     vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
#         a.clear();
#         int n=words.size(),m=puzzles.size(),i,j,k;
#         ans.resize(m,0);
#         for(i=0;i<n;i++)
#         {
#             for(j=k=0;j<words[i].size();j++)k|=1<<words[i][j]-'a';
#             a[k]++;
#         }
#         for(i=0;i<m;i++)
#         {
#             for(j=k=0;j<puzzles[i].size();j++)k|=1<<puzzles[i][j]-'a';
#             for(j=k;j;j=j-1&k)if(j>>puzzles[i][0]-'a'&1)ans[i]+=a[j];
#         }
#         return ans;
#     }
# };


s = Solution()
print(s.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
# print(s.findNumOfValidWords2(words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))