def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    height_sort = height.copy()
    height_sort.sort()
    if len(height)<2:
        return 0

    high_est = height_sort[-1]
    # print("highest", high_est)
    second_highest = height_sort[-2]
    # print("second", second_highest)
    print(height)

    if second_highest == 0:
        return 0

    high_est_index = height.index(high_est)
    second_highest_index = height.index(second_highest)
    if second_highest!=high_est:
        if high_est_index > second_highest_index:
            right_point = high_est_index
            left_point = second_highest_index
        elif high_est_index < second_highest_index:
            left_point = high_est_index
            right_point = second_highest_index
        else:
            return 0
    else:
        index_list = [i for i, t in enumerate(height) if t==high_est]
        if len(index_list)<2:
            return 0
        else:
            left_point = index_list[0]
            right_point = index_list[1]

    emerge = 0
    print("left:",left_point)
    print("right:",right_point)
    for i in range(left_point+1, right_point):
        emerge += height[i]
    # print(emerge)
    print(second_highest*(right_point-left_point-1)-emerge)
    mid_area = second_highest*(right_point-left_point-1)-emerge
    print("mid",mid_area)

    if left_point>0:
        left_part = trap(height[:left_point+1])
    else:
        left_part = 0
    if right_point<len(height):
        right_part = trap(height[right_point:])
    else:
        right_part = 0

    return left_part+right_part+ mid_area

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([2,1,2,1]))