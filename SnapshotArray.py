class SnapshotArray:

    def __init__(self, length: int):
        self.buffer = [0 for _ in range(length)]
        self.snap_count = -1
        self.snap_id_dict = {}

    def set(self, index: int, val: int) -> None:
        self.buffer[index] = val

    def snap(self) -> int:
        self.snap_count += 1
        self.snap_id_dict[self.snap_count] = [x for x in self.buffer]
        return self.snap_count

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_id_dict[snap_id][index]


class SnapshotArray2:

    def __init__(self, length: int):
        self.snap_count = -1
        self.buffer = [{-1: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.buffer[index][self.snap_count] = val

    def snap(self) -> int:
        for each in self.buffer:
            each[self.snap_count + 1] = each[self.snap_count]
        self.snap_count += 1
        return self.snap_count

    def get(self, index: int, snap_id: int) -> int:
        return self.buffer[index][snap_id - 1]


# 两次超时
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

import bisect
class SnapshotArray3(object):
    # from answer
    def __init__(self, length):
        """
        :type length: int
        """
        self.arr = [[0] for _ in range(length)]
        self.time = [[0] for _ in range(length)]
        self.count = 0
        # print self.arr, self.time

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.count == self.time[index][-1]:
            self.arr[index][-1] = val
            return
        self.arr[index].append(val)
        self.time[index].append(self.count)

    def snap(self):
        """
        :rtype: int
        """
        self.count += 1
        return self.count - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        pick = bisect.bisect_left(self.time[index], snap_id)
        # print self.arr, self.time, pick
        if pick >= len(self.arr[index]):
            return self.arr[index][-1]
        if self.time[index][pick] > snap_id:
            pick -= 1
            if pick < 0:
                pick += 1
        return self.arr[index][pick]

