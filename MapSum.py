class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_word = {}
        self.dict_trie = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key not in self.dict_word:
            self.dict_word[key] = val
            for i in range(len(key)):
                if key[:i] not in self.dict_trie:
                    self.dict_trie[key[:i]] = val
                else:
                    self.dict_trie[key[:i]] += val
        else:
            old_Val = self.dict_word[key]
            self.dict_word[key] = val
            for i in range(len(key)):
                if key[:i] not in self.dict_trie:
                    self.dict_trie[key[:i]] = val
                else:
                    self.dict_trie[key[:i]] += val - old_Val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # print(self.dict_trie)
        # print(self.dict_word)
        res = 0
        if prefix in self.dict_trie:
            res += self.dict_trie[prefix]
        if prefix in self.dict_word:
            res += self.dict_word[prefix]

        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)