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
            time_check = 0

            need_to_go = []
            for each in this_list:
                if count[each] == 0:
                    need_to_go.append(each)
                else:
                    count[each] -= 1
                    total_time += 1
                    time_check += 1

                if time_check == n:
                    break

            print(count, total_time, time_check)

            for each_zero in need_to_go:
                count.pop(each_zero)

            if not count:
                return total_time

            if time_check < n:
                total_time += n - time_check




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


