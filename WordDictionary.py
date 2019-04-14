class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        t = self.root
        for i in word:
            if i not in t:
                t[i] = {}

            t = t[i]
        t['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def find(word=word, t=self.root):
            if not word:
                return '#' in t
            if len(t) == 1 and '#' in t and len(word) > 0:
                return False
            if word[0] in t and word[0] != '.' and find(word[1:], t[word[0]]):
                return True
            if word[0] == '.':
                for i in t.keys():
                    if i != '#' and find(word[1:], t[i]):
                        return True
            return False

        return find()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)