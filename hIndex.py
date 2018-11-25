class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations:
            return 0
        citations.sort(reverse=True)


        total_num = len(citations)
        # print(citations)
        number_list = {}

        num_init = citations[0]
        for i in range(len(citations)):
            if citations[i] != num_init:
                number_list[num_init] = i
                num_init = citations[i]
            else:
                pass


        if num_init not in number_list:
            number_list[num_init] = total_num

        print(number_list)

        keys = list(number_list.keys())
        keys.sort(reverse=True)

        h_list = []
        for each in keys:
            h_list.append(min(number_list[each], each))

        return max(h_list)







s = Solution()
print(s.hIndex([4,4,0,0]))
