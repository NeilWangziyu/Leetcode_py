from typing import List
import collections
class Solution:
    r = []
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.r = []
        if not tickets:
            return []
        if len(tickets) == 1:
            return tickets[0]
        total_filght = len(tickets)
        all_map = {}
        for each in tickets:
            if each[0] not in all_map:
                all_map[each[0]] = [each[1]]
            else:
                all_map[each[0]].append(each[1])

        for each in all_map.keys():
            all_map[each].sort()
        # print(all_map)
        res = ["JFK"]
        init_flight = "JFK"
        used_flight = 0

        def DSF(init_flight, all_map, res, used_flight, total_filght):
            if self.r != []:
                return
            if init_flight not in all_map or all_map[init_flight] == []:
                if used_flight == total_filght:
                    self.r.append(res)
                else:
                    return
            else:
                for i in range(len(all_map[init_flight])):
                    tem = all_map[init_flight].pop(i)
                    DSF(tem, all_map, res+[tem], used_flight+1, total_filght)
                    all_map[init_flight].insert(i, tem)

        DSF(init_flight, all_map, res, used_flight, total_filght)
        return self.r[0]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        trips = collections.defaultdict(list)
        for ticket in tickets:
            trips[ticket[0]].append(ticket[1])
        for key in trips.keys():
            trips[key].sort()
        self.ans = []

        def visit(s):
            dests = trips[s]
            while len(dests):
                dest = dests[0]
                dests.pop(0)
                visit(dest)
            self.ans.append(s)

        visit('JFK')

        self.ans.reverse()
        return self.ans


s = Solution()
print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# ["JFK","NRT","JFK","KUL"]