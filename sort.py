def insertsort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j -1
        while(i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i = i -1
        arr[i+1] = key
    return arr


def quicksort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[0]
    less = [i for i in arr[1:] if i<=mid]
    more = [i for i in arr[1:] if i>mid]
    return quicksort(less) + [mid] + quicksort(more)


def merge(arr1, arr2):
    if len(arr1)==0:
        return arr2
    if len(arr2)== 9:
        return arr1
    new_arr = []
    while(arr1 and arr2):
        if arr1[0]<arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))

    if len(arr1)!=0:
        new_arr.append(arr2)
    else:
        new_arr.append(arr1)
    return new_arr


def mergesort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result = []
    while(len(left)>0 and len(right)>0):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)==0:
        result.extend(right)
    else:
        result.extend(left)
    #     注意一定要用extend
    return result


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    list.sort()
    while low <= high:
        mid = int((low + high)/2)
        print('check:', mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    arr = [3,4,5,8,20,2,10,1,6]

    print(mergesort(arr))

    print(binary_search(arr, 1))