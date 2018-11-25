def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def swap(i, j, nums):
        x = nums.copy()
        tem = x[i]
        x[i] = x[j]
        x[j] = tem
        return x

    res = [nums]
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            print(i, j)
            if i==0:
                res.append(swap(i, j, nums))
            else:
                tem = []
                for each in res:
                    print("each", each)
                    if j!=i+1:
                        tem.append(swap(i, j, each))
                res = res + tem
            print("res",res)
    res.sort()
    return res


print(permute([1,2,3,4]))