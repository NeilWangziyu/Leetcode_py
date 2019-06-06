class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None

        length = len(arr)
        if length == 1:
            return 1

        arr_in_order = list(range(length))
        # print(arr_in_order)
        count = 1
        for i in range(1, length):
            if set(arr[:i]) == set(range(i)):
                # print("i",i)
                count += 1


        return count

    def maxChunksToSorted2(self, arr) -> int:
        res = 1
        left_max = arr[0]
        for i in range(len(arr) - 1):
            left_max = max(left_max, arr[i])
            if left_max == i:
                res += 1
        return res


s = Solution()
print(s.maxChunksToSorted([4,3,2,1,0]))
print(s.maxChunksToSorted([1,0,2,3,4]))