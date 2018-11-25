def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    def reverseword(word):
        new_list = []
        for each in word:
            new_list.insert(0, each)
        return ''.join(new_list)

    word_list = s.split(" ")
    new_word_list = []
    for each in word_list:
        new_word_list.append(reverseword(each))

    return ' '.join(new_word_list)



print(reverseWords("hello nihao"))