# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0
        intervals_sorted = sorted(intervals, key=lambda x:x.end)
        init_check = intervals_sorted[0].end
        res = 0
        for i in range(1, len(intervals_sorted)):
            if intervals_sorted[i].start < init_check:
                res += 1
            else:
                init_check = intervals_sorted[i].end
        return res




if __name__ == "__main__":
    s = Solution()
    intervals =[ [1,2], [2,3], [6, 9], [7, 10] ]
    print(s.eraseOverlapIntervals(intervals))