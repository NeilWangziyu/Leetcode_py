def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    wordlist = [each for each in s]
    # print(wordlist)

    vo = ['a','e','i','o','u']
    i = 0
    j = len(wordlist)-1
    while(i<j):
        while(wordlist[i] not in vo):
            i += 1
            if (i > len(wordlist)-1):
                break
        while(wordlist[j] not in vo):
            j -= 1
            if j<0:
                break
        if (i>=j):
            break
        tem = wordlist[i]
        wordlist[i] = wordlist[j]
        wordlist[j] = tem
        i += 1
        j -= 1

    print(wordlist)
    return wordlist



reverseVowels("OE")
