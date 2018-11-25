def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "" or s==" ":
        return 0
    else:
        s_split = s.split(' ')
        print(s_split)
        while s_split[-1]=='':
            s_split.pop(-1)
            if len(s_split) == 1:
                break

        if s_split == "" or s_split==" ":
            return 0
        else:
            return len(s_split[-1])

lengthOfLastWord(" a")
