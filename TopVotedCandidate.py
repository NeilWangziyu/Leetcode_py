class TopVotedCandidate:
    # 超时
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.count = {}
        for index, person in enumerate(persons):
            if person not in self.count:
                self.count[person] = []
            self.count[person].append(times[index])
        # print(self.count)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """

        def binquery(time_list, t):
            if not time_list:
                return 0,0
            if time_list[0] > t:
                return 0,0
            elif time_list[0] == t:
                return 1,time_list[0]
            else:
                if len(time_list) == 1:
                    return 1, time_list[0]
                elif t >= time_list[-1]:
                    return len(time_list), time_list[-1]
                else:
                    low = 0
                    high = len(time_list) - 1
                    while (low <= high):
                        mid = (low + high) // 2
                        if time_list[mid] == t:
                            return mid + 1, time_list[mid]
                        elif time_list[mid] > t:
                            high = mid - 1
                        else:
                            low = mid + 1
                    # print(low, high,time_list[(low + high) // 2])
                    return (low + high) // 2 + 1, time_list[(low + high) // 2]

        # print(self.count)
        max_count = 0
        prev_latest_time = 0
        max_person = None
        for each in self.count.keys():
            each_ticket, latest_time = binquery(self.count[each], t)
            # print(each, each_ticket)
            if each_ticket > max_count:
                max_count = each_ticket
                max_person = each
                prev_latest_time = latest_time
            elif each_ticket == max_count:
                # print(latest_time, prev_latest_time)
                if latest_time > prev_latest_time:
                    prev_latest_time = latest_time
                    max_person = each
        return max_person




# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

class TopVotedCandidate2(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # self.persons = persons
        self.times = times
        self.winner = []
        premax = 0
        prewin = None
        tmp = [0] * len(persons)
        for i in persons:
            tmp[i] += 1
            if tmp[i] >= premax:
                self.winner.append(i)
                prewin = i
                premax = tmp[i]
            else:
                self.winner.append(prewin)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        index = self.getTimesIndex(t)
        return self.winner[index]

    def getTimesIndex(self, t):
        if t in self.times:
            return self.times.index(t)
        elif self.times[-1] < t:
            return -1
        else:
            l, r = 0, len(self.times) - 1
            while (r - l) > 1:
                mid = (l + r) // 2
                if self.times[mid] < t:
                    l = mid
                else:
                    r = mid
            return l



class TopVotedCandidate3:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        sorted_persons = persons[:]
        sorted_times = times[:]

        if not persons or not times:
            self.vailid = False
        else:
            self.vailid = True
        tmp = list(range(len(times)))
        tmp = sorted(tmp, key=lambda i:times[i])
        for i in tmp:
            sorted_persons[i]=persons[i]
            sorted_times[i]=times[i]
        self.times = sorted_times
        persons_number = max(persons)
        score_table = [0]*(persons_number+1)
        self.winner = [0]*len(times)
        max_til_now = 0
        now_winner = 0
        for i in range(len(times)):
            score_table[sorted_persons[i]]+=1
            if score_table[sorted_persons[i]]>max_til_now:
                max_til_now=score_table[sorted_persons[i]]
                now_winner = sorted_persons[i]
            elif score_table[sorted_persons[i]]==max_til_now:
                now_winner = sorted_persons[i]
            self.winner[i] = now_winner

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if not self.vailid:
            return -1
        if t>=self.times[-1]:
            return self.winner[-1]
        if t<=self.times[0]:
            return self.winner[0]

        l = 0
        r = len(self.times)
        while(l<r):
            mid = (l+r)//2
            if self.times[mid]<=t:
                l=mid+1
            else:
                r=mid
        return self.winner[l-1]



class TopVotedCandidate4:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        n = len(persons)
        nums = [0]*(n+1)
        self.top = [0]*n
        tmp = 0
        for i in range(n):
            nums[persons[i]] += 1
            if nums[persons[i]]>=nums[tmp]:
                tmp = persons[i]
            self.top[i] = tmp

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)
        return self.top[idx-1]



def binquery(time_list, t):
    if not time_list:
        return 0, 0
    if time_list[0] > t:
        return 0, 0
    elif time_list[0] == t:
        return 1, time_list[0]
    else:
        if len(time_list) == 1:
            return 1, time_list[0]
        elif t >= time_list[-1]:
            return len(time_list), time_list[-1]
        else:
            low = 0
            high = len(time_list) - 1
            while (low <= high):
                mid = (low + high) // 2
                if time_list[mid] == t:
                    return mid + 1, time_list[mid]
                elif time_list[mid] > t:
                    high = mid - 1
                else:
                    low = mid + 1
            # print(low, high,time_list[(low + high) // 2])
            return (low + high) // 2 + 1, time_list[(low + high) // 2]


print(binquery([0, 15, 20, 30], 15))
# {0: [0, 15, 20, 30], 1: [5, 10, 25]}
