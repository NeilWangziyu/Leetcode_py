class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return arr
        count = len(arr)
        number = 0
        while(count > 0):
            each = arr.pop(0)
            if each != 0:
                arr.append(each)
                count -= 1
            else:
                arr.append(each)
                arr.append(each)
                count -= 1
                number += 1
        for _ in range(number):
            arr.pop(-1)
        print(arr)

    def duplicateZeros2(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return arr
        new_Arr = []
        count = len(arr)
        number = 0
        for each in arr:
            if each != 0:
                new_Arr.append(each)
                count -= 1
            else:
                new_Arr.append(each)
                new_Arr.append(each)
                count -= 1
                number += 1

        arr = new_Arr[:len(new_Arr) - number]
        print(arr)


s = Solution()
arr = [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(arr))
print(s.duplicateZeros2(arr))


arr = [8,4,5,0,0,0,0,7]
print(s.duplicateZeros(arr))
print(s.duplicateZeros2(arr))

