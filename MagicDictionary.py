from typing import List

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.dict = {}

        check_list = set("abcdefghijklmnopqrstuvwxyz")
        for each in dict:
            length = len(each)
            for i in range(length):
                replace_c = each[i]
                for each_different_c in check_list:
                    if each_different_c != replace_c:
                        tem = each[:i] + each_different_c + each[i + 1:]
                        self.dict[tem] = True

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if word not in self.dict:
            return False
        else:
            return True

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
if __name__ == "__main__":
    s = MagicDictionary()

    s.buildDict(["hello", "leetcode"])

    print(s.dict)

    print(s.search("hello"))
    print(s.search("helle"))
    print(s.search("helloo"))

    print(s.search("lietcode"))
