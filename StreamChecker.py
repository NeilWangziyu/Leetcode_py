class StreamChecker0:
    def __init__(self, words):
        self.ourdict = set()
        self.length = 0
        self.stack_list = []
        for each in words:
            if len(each) > self.length:
                self.length = len(each)
            self.ourdict.add(each)


    def query(self, letter: str) -> bool:
        if len(self.stack_list) < self.length:
            self.stack_list.append(letter)
        else:
            self.stack_list.pop(0)
            self.stack_list.append(letter)
        for i in range(len(self.stack_list)):
            check = "".join(self.stack_list[i:])
            if check in self.ourdict:
                return True
        return False


class StreamChecker1:
    def __init__(self, words):
        self.ourdict = set()
        self.length = 0
        self.stack_list = ""
        for each in words:
            if len(each) > self.length:
                self.length = len(each)
            self.ourdict.add(each)


    def query(self, letter: str) -> bool:
        if len(self.stack_list) < self.length:
            self.stack_list += letter
        else:
            self.stack_list = self.stack_list[1:]
            self.stack_list += letter

        for i in range(len(self.stack_list)):
            check = self.stack_list[i:]
            if check in self.ourdict:
                return True
        return False


        # if letter in self.ourdict:
        #     return True
        # else:
        #     return False


class Trie(object):
    def __init__(self, words):
        self.data = [None] * 27
        for word in words:
            layer = self.data
            for char in word:
                index = ord(char) - ord('a')
                if layer[index] is None:
                    layer[index] = [None] * 27
                layer = layer[index]
            layer[-1] = True


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie(words)
        self.poss = [self.trie.data]

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        nposs = list()
        index = ord(letter) - ord('a')
        ans = False
        for poss in self.poss:
            if poss[index] is not None:
                if poss[index][-1]:
                    ans = True
                nposs.append(poss[index])
        nposs.append(self.trie.data)
        self.poss = nposs
        return ans

# class StreamChecker:
#     def __init__(self, words):
#         self.trie = {}
#         self.end_of_word = '#'
#         self.length = 0
#         self.stack_list = ""
#
#         for word in words:
#             if len(word) > self.length:
#                 self.length = len(word)
#             node = self.trie
#             for char in word:
#                 node = node.setdefault(char, {})
#             node[self.end_of_word] = self.end_of_word
#         # print(self.trie)
#
#
#     def query(self, letter: str) -> bool:
#         if len(self.stack_list) < self.length:
#             self.stack_list += letter
#         else:
#             self.stack_list = self.stack_list[1:]
#             self.stack_list += letter
#
#         for i in range(len(self.stack_list)):
#             found = False
#             check = self.stack_list[i:]
#             searchword = self.trie
#
#             for w in check:
#                 if w in searchword:
#                     searchword = searchword[w]
#                     found = True
#                 else:
#                     found = False
#                     continue
#
#             if found == True and self.end_of_word in searchword:
#                 return True
#             else:
#                 continue
#         return False





            # Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# s = StreamChecker0(["cd","f","kl"])
# t = StreamChecker(["cd","f","kl"])
#
# check_list = list("abcdefghijkl")
# for each in check_list:
#     print(each)
#     print(t.query(each))
#
#
# s = StreamChecker0(["ab","ba","aaab","abab","baa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"])
# t = StreamChecker(["ab","ba","aaab","abab","baa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"])
#
# check_list = list("aaaaabbbbbaaaaabbbb")
# for each in check_list:
#     if s.query(each) != t.query(each):
#         print("Wrong")



# ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
# [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
# [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]