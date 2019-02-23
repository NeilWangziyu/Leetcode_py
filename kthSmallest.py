class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        # 排序队列
        def rank(list_prio, num):
            if list_prio == []:
                return 0
            if num <= list_prio[0]:
                return 0
            if num >= list_prio[-1]:
                return len(list_prio)
            low = 0
            high = len(list_prio)
            while(low <= high):
                mid = (low + high) // 2
                if list_prio[mid] == num:
                    return mid
                elif list_prio[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        if k == 1:
            return matrix[0][0]

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(res) < k:

                    res.insert(rank(res, matrix[i][j]), matrix[i][j])
                else:
                    if res[-1] <= matrix[i][j]:
                        continue
                    else:
                        res.pop(-1)
                        res.insert(rank(res, matrix[i][j]), matrix[i][j])
                print(res)
            print(len(res))
        return res[-1]

    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        l = []
        for i in matrix:
            l.extend(i)
        l.sort()
        return l[k - 1]




s = Solution()
matrix = [[3,3,8,13,13,18],[4,5,11,13,18,20],[9,9,14,15,23,23],[13,18,22,22,25,27],[18,22,23,28,30,33],[21,25,28,30,35,35]]



k = 21
print(s.kthSmallest(matrix, k))