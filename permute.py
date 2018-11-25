def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    set_num = list(set(nums))
    set_num.sort()
    print(set_num)
    mis_list = []
    i = 0
    while i<len(nums):
        print(i)
        if set_num[i]!=i+1:
            print("!',i")
            for t in range(i, set_num[i]):
                mis_list.append(t)
            i = set_num[i]-1
        else:
            i += 1
    return mis_list


nums = [1,1,2,3,5]

print(permute(nums))