def max_cross_subarray(arr, low, high, mid):
    cross_high = mid+1
    cross_low = mid
    left_sum = arr[mid]
    sum = 0
    i = mid

    while(i>=low):
        sum += arr[i]
        if sum >= left_sum:
            left_sum = sum
            cross_low = i
        i -= 1

    right_sum = arr[mid+1]
    sum = 0
    for j in range(mid+1, high+1):
        sum += arr[j]
        if sum >= right_sum:
            right_sum = sum
            cross_high = j
    cross_sum = right_sum + left_sum

    return (cross_low, cross_high, cross_sum)



def max_subarray(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    else:
        mid = (high + low) // 2
        print(mid)
        (left_low, left_high, left_sum) = max_subarray(arr, low, mid)

        (right_low, right_high, right_sum) = max_subarray(arr, mid+1, high)

        (cross_low, cross_high, cross_sum) = max_cross_subarray(arr, low, high, mid)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        if right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)




arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print("length",len(arr))
print(max_subarray(arr, 0, len(arr)-1))

print(sum(arr[7:11]))


print(max_cross_subarray([1,1,1,1,1], 0, 4, 2))

