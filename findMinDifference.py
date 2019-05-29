class Solution:
    def findMinDifference(self, timePoints) -> int:
        minute_list = []
        max_minute = 0
        min_minute = float('inf')
        for each in timePoints:
            each_split = each.split(":")
            hour = int(each_split[0])
            minute = int(each_split[1])
            # print(hour, minute)
            total_minute = hour * 60 + minute
            minute_list.append(total_minute)
            max_minute = max(total_minute, max_minute)
            min_minute = min(total_minute, min_minute)

        # print(minute_list)

        # minute_list.insert(0, (60*24 - max_minute))
        minute_list.sort()

        # print(minute_list)
        res = float('inf')
        for i in range(1, len(minute_list)):
            res = min(minute_list[i] - minute_list[i-1], res)
        res = min(res,  (60*24+min_minute - max_minute))
        return res

    def findMinDifference2(self, timePoints) -> int:
        time = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        sub_time = [time[i + 1] - time[i] for i in range(len(time) - 1)]
        a = time[-1] - time[0]
        if a > 720:
            a = 1440 - a
        sub_time.append(a)
        return min(sub_time)


timePoints = ["12:12","00:13"]
s = Solution()
print(s.findMinDifference(timePoints))