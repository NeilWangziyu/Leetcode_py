class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A) // 2
        if length == 1:
            return A[0]
        dict_a = {}
        for each in A:
            if each not in dict_a:
                dict_a[each] = 1
            else:
                dict_a[each] += 1
                if dict_a[each] == length:
                    return each