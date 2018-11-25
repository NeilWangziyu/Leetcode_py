class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # if not citations:
        #     return 0
        #
        #
        # total_num = len(citations)
        # # print(citations)
        # number_list = {}
        #
        # num_init = citations[0]
        # prev = 0
        # for i in range(len(citations)):
        #     if citations[i] != num_init:
        #         number_list[num_init] = total_num - prev
        #         num_init = citations[i]
        #         prev = i
        #     else:
        #         pass
        #
        #
        # if num_init not in number_list:
        #     number_list[num_init] = total_num - prev
        #
        # print(number_list)
        #
        # keys = list(number_list.keys())
        # keys.sort(reverse=True)
        #
        # h_list = []
        # for each in keys:
        #     h_list.append(min(number_list[each], each))
        #
        # return max(h_list)

        start, end = 1, len(citations)
        while start <= end:
            h = int((start + end) // 2)
            if citations[len(citations) - h] < h:  # h应该更小
                end = h - 1
            elif len(citations) - h - 1 >= 0 and citations[len(citations) - h - 1] > h:  # h应该更大
                start = h + 1
            else:
                return h
        return 0


s = Solution()
print(s.hIndex([0,1,3,5,6]))