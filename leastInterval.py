from typing import List
import collections

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        if n == 0:
            return len(tasks)

        from collections import Counter

        if not tasks:
            return 0

        count = Counter(tasks)
        total_time = 0

        while(count):
            this_list = count.keys()
            this_list = sorted(this_list, key=lambda x:count[x], reverse=True)
            time_check = -1

            need_to_go = []
            for each in this_list:
                if count[each] == 0:
                    need_to_go.append(each)
                else:
                    count[each] -= 1
                    total_time += 1
                    time_check += 1
                    if count[each] == 0:
                        need_to_go.append(each)


                if time_check == n:
                    break

            # print(count, total_time, time_check,need_to_go)

            for each_zero in need_to_go:
                count.pop(each_zero)

            if not count:
                return total_time

            if time_check < n:
                total_time += n - time_check

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        # 在任务最多的那个插空，每个空档长度（算上本身）为n+1，
        # 若和最大次数相同的有多个，则在末尾溢出
        # 任务种数超过n+1时，每个空档容不下次数少于最大次数的任务，会放在末尾，可能超过上面的计算长度
        counters = collections.Counter(tasks)
        maxCnt = counters.most_common(1)[0][1]

        extra = 0
        for i in counters:
            if counters[i] == maxCnt:
                extra += 1

        return max(len(tasks), (maxCnt - 1) * (n + 1) + extra)


tasks = ["A","B","C","D","E","A","B","C","D","E",'A']

n = 4
s = Solution()
print(s.leastInterval(tasks, n))

tasks = ["A","A","A","B","B","B"]
n = 2
print(s.leastInterval(tasks, n))

tasks =["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(s.leastInterval(tasks, n))
# 16
tasks = ["A","A","A","B","B","B"]
n = 2
# 8
print(s.leastInterval(tasks, n))



