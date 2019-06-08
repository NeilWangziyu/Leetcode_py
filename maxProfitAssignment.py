class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        work_list = []
        for i in range(len(difficulty)):
            work_list.append([difficulty[i], profit[i]])
        work_list.sort(reverse=True, key=lambda x:x[1])
        worker.sort(reverse=True)
        res = 0
        check = 0
        init = 0
        while(check < len(worker)):
            while(init < len(work_list) and worker[check] < work_list[init][0]):
                init += 1
            if init >= len(work_list) :
                check += 1
            else:
                res += work_list[init][1]
                # print(init, check, work_list[init], worker[check])
                check += 1
        return res

    def maxProfitAssignment2(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        from collections import Counter
        li = sorted(zip(profit, difficulty))
        ret = 0
        worker = Counter(worker)
        for i in sorted(worker, reverse=True):
            while li and li[-1][1] > i:
                li.pop()
            if li:
                ret += li[-1][0] * worker[i]
            else:
                break
        return ret


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]

s = Solution()
print(s.maxProfitAssignment(difficulty, profit, worker))
