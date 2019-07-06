class RecentCounter:

    def __init__(self):
        self.res = []

    def ping(self, t):
        """
        这题傻逼了，没有注意到t后面的都比前面的大，还去比大小了
        :type t: int
        :rtype: int
        """
        while (self.res):
            if self.res[0] < t - 3000:
                self.res.pop(0)
            else:
                break

        if self.res == []:
            self.res.append(t)
            return 1
        else:
            if t < self.res[0]:
                self.res.insert(0, t)
                return 0
            elif t > self.res[-1]:
                self.res.append(t)
                return len(self.res)
            else:
                start = 0
                end = len(self.res) - 1
                while (self.res[start] <= self.res[end]):
                    mid = (start + end) // 2
                    if self.res[mid] > t:
                        end = mid - 1
                    elif self.res[mid] < t:
                        start = mid + 1
                    else:
                        self.res.insert(mid, t)
                        return mid + 1
                self.res.insert(start, t)
                return start + 1

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)