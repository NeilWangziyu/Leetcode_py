def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
        return 1
    else:
        half = x // 2 + 1
        for i in range(half):
            if x >= i ** 2 and x < (i + 1) ** 2:
                return i
            else:
                pass


def mySqrt_2(x):
    if x == 1:
        return 1
    else:
        low = 1
        high = x
        while(high>low):
            mid = (low+high)//2
            if x<mid**2:
                high = mid
            else:
                low = mid+1
        return high - 1




print(mySqrt(515404582))
print(mySqrt_2(515404582))