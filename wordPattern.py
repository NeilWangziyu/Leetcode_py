def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    pattern = [each for each in pattern]
    str_new = str.split(" ")
    print(pattern)
    print(str_new)

    dict_use = {}
    str_use = {}

    N = len(str_new)
    M = len(pattern)
    if N != M:
        return False
    for i in range(N):
        if pattern[i] in dict_use:
            if dict_use[pattern[i]] != str_new[i]:
                return False
        else:
            print(pattern[i])
            if str_new[i] in str_use:
                return False
            else:
                dict_use[pattern[i]] = str_new[i]
                str_use[str_new[i]] = pattern[i]
    return True




print(wordPattern(pattern="abba", str="dog cat cat dog"))