class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        return words == sorted(words, key=lambda x: list(map(order.index, x)))

    def isAlienSorted2(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))



#
#
# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
# words = ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
words = ["urzfepcbikcd","zirxpxirgvenb","gkyoejecyp","nycojipakqqs","ffvriqqlcncybz","lhgzremfpvzfkgpgli","bakszbtncnbliwxjf","jeacyyaiclxidyxig","opkuspsremeqkbvkwoe","pdlfvjorsdmoeuwhs"]
order = "dopausthvemniyxqwkfjczrglb"
s = Solution()
print(s.isAlienSorted2(words, order))
