def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    print(len(deck))
    if len(deck)<2:
        return False
    else:
        dict_list = {}
        for i in range(len(deck)):
            if deck[i] in dict_list:
                dict_list[deck[i]] += 1
            else:
                dict_list[deck[i]] = 1
    print(dict_list)
    nums = [dict_list[each] for each in dict_list]
    print(nums)
    minmin = min(nums)
    print(minmin)
    flag = 1
    #表示可以
    for i in range(2, max(minmin+1,3)):
        print(i)
        for index in range(len(nums)):
            print("index:",index)
            if nums[index]%i != 0:
                flag = 0
                break

        if flag == 1:
            return True
        flag = 1

    return False





print(hasGroupsSizeX([1,1,1,2,2,2]))
