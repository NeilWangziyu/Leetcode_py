def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0
    if nums:
        nums.sort()
        print(nums)
        i = 0
        count = 0
        max_pre = 0
        res = 0
        change = True
        differ = False
        if len(nums) > 0:
            base = nums[0]
            while (i < len(nums)):
                print("i:", i)
                if nums[i] == base:
                    count += 1
                    i += 1
                    if i == len(nums):
                        print("!")
                        if differ == True and change == True and max_pre + count > res:
                            print(max_pre)
                            res = max_pre + count


                else:
                    # start to change
                    differ = True
                    if change == True and max_pre + count > res:
                        res = max_pre + count
                    if nums[i] == base + 1:
                        change = True
                    else:
                        change = False
                    max_pre = count
                    base = nums[i]
                    count = 1
                    i += 1
                print('count', count)
                print(res)
            return res
        else:
            return 0

re = findLHS([1,3])
print(re)


