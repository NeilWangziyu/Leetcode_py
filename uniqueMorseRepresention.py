def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    def return_morse(word):
        morse_li = []
        for each_character in word:
            morse_li.append(morse_dict[each_character])
        return "".join(morse_li)


    alphabeta = [chr(i) for i in range(97, 123)]
    # print(alphabeta)
    morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
     "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    morse_dict = {}
    i = 0
    for each in alphabeta:
        morse_dict[each] = morse_list[i]
        i += 1

    word_morse_dict = {}
    print(words)
    count = 0
    for word in words:
        morse = return_morse(word)
        print(morse)
        if morse in word_morse_dict:
            word_morse_dict[morse] += 1
        else:
            count += 1
            word_morse_dict[morse] = 1

    return count




words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))