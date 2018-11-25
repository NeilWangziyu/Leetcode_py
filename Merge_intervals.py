class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self,intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals_list = []
        for each in intervals:
            tem_intervals = Interval(each[0], each[1])
            intervals_list.append(tem_intervals)


if __name__ == '__main__':
    # a = Interval(1,4)
    # b = Interval(4,5)
    # list = []
    # list.append(a)
    # list.append(b)

    s = Solution()
    s.merge([[1,3],[2,6],[8,10],[15,18]])
