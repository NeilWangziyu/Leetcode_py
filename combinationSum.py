def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(candidates) == 1:
        if candidates[0] == target:
            return [[candidates[0]]]
        else:
            return []

    res = []
    min_num = min(candidates)
    # for each in candidates:

    # for i in range(len(candidates)):

    while(candidates):
        print(candidates)
        if target - candidates[0] == 0:
            res.append([candidates[0]])
        else:
            if target - candidates[0] >= min_num:
                ans_list = combinationSum(candidates.copy(), target - candidates[0])
                for each_ans in ans_list:
                    print([candidates[0]],each_ans)
                    res.append([candidates[0]]+each_ans)

        candidates.pop(0)
    return res


print(combinationSum(candidates = [1,2], target = 4))