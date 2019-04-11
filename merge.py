# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]
        i = 0
        while (i < len(intervals)):
            while (i < len(intervals) and result[-1].end >= intervals[i].start):
                if result[-1].end < intervals[i].end:
                    result[-1] = Interval(result[-1].start, intervals[i].end)
                else:
                    result[-1] = Interval(result[-1].start, result[-1].end)
                i += 1
            if i < len(intervals):
                result.append(intervals[i])

        return result

    def merge2(self, intervals: List[Interval]) -> List[Interval]:

        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)

        res = [Interval(intervals[0].start, intervals[0].end)]

        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                if intervals[i].end > res[-1].end:
                    res[-1] = Interval(res[-1].start, intervals[i].end)
                else:
                    pass
            else:
                res.append(intervals[i])

        return res

    def merge3(self, intervals: 'List[Interval]') -> 'List[Interval]':
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(i.end, res[-1].end)
            else:
                res.append(i)
        return res


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
s = Solution()
print(s.merge(intervals))

