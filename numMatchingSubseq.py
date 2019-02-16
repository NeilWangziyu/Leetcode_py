class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dict = {}
        def DFS(depth, start, res_list):
            dict[res_list] = True
            if depth == len(S):
                return
            for i in range(start, len(S)):
                DFS(depth+1, i+1, res_list+S[i])

        DFS(0, 0, "")
        print(dict)
        res = 0
        for each in words:
            if each in dict:
                res += 1
        return res


    def numMatchingSubseq2(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter
        count = 0
        words = Counter(words)
        print(words)
        for word, num in words.items():
            start = 0
            flag = False
            for alp in word:
                print(alp)
                start = S.find(alp, start) + 1
                if start == 0:
                    flag = True
                    break
            if not flag:
                count += num
        return count


#
# S = "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac"
# words = ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]

S = "abcde"
words = ["a", "bb", "acd", "ace"]

s = Solution()
print(s.numMatchingSubseq2(S, words))