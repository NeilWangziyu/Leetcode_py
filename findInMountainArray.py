# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# 迷之报错...太奇怪了真的

class Solution:
    def findl(self, mountain_arr, l, r, target):
        if l > r:
            return -1
        k = (l + r) // 2
        tmp = mountain_arr.get(k)
        if tmp == target:
            return k

        while (tmp != target and r - l >= 1):
            if target > tmp:
                l = k + 1
            else:
                r = k - 1
            k = (l + r) // 2
            print(l, r, k)
            tmp == mountain_arr.get(k)
            if tmp == target:
                return k
        return -1

    def findr(self, mountain_arr, l, r, target):
        print(l, r)

        if l > r:
            return -1
        k = (l + r) // 2
        tmp = mountain_arr.get(k)
        if tmp == target:
            return k

        while (tmp != target and r - l >= 1):
            if target < tmp:
                l = k + 1
            else:
                r = k - 1
            k = (l + r) // 2
            print(l, r, k)
            tmp == mountain_arr.get(k)
            if tmp == target:
                return k
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:


        n = mountain_arr.length()
        left = 0
        right = n - 1
        k = (left + right) // 2
        tmp = mountain_arr.get(k)
        while (not (tmp > mountain_arr.get(k - 1) and tmp > mountain_arr.get(k + 1))):
            if mountain_arr.get(k + 1) > tmp:
                left = k + 1
            else:
                right = k
            k = (left + right) // 2
            tmp = mountain_arr.get(k)
        print(k)
        med = k
        ll = self.findl(mountain_arr, 0, med, target)
        rr = self.findr(mountain_arr, med, n - 1, target)

        if ll != -1:
            return ll
        else:
            return rr

