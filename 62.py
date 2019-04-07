# Josephuse circle
def LastRemaining(n, m):
    if n < 1 or m < 1:
        return -1
    nums = [i for i in range(n)]
    init = 0
    while(len(nums)>1):
        init += (m - 1)
        init = init % len(nums)
        nums.pop(init)
    return nums[0]

def LastRemaining_function(n, m):
    if n < 1 or m < 1:
        return 0
    last = 0
    for i in range(2, n+1):
        last = (last + m )% i
    return last



if __name__ == "__main__":
    n = 12
    m = 3
    print(LastRemaining(n, m))
    print(LastRemaining_function(n, m))