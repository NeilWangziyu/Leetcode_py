class Solution:
    def numFriendRequests(self, ages) -> int:
        """
        超时
        :param ages:
        :return:
        """
        if not ages:
            return  0
        res = 0
        for i in range(len(ages)):
            for j in range(i+1, len(ages)):
                if ages[i]<=0.5*ages[j]+7 or ages[i] > ages[j]:
                    pass
                else:

                    res += 1

                if ages[j] <= 0.5*ages[i] + 7 or ages[j] >ages[i]:
                    pass
                else:
                    res += 1
        return res

    def numFriendRequests2(self, ages) -> int:
        if not ages:
            return 0

        from collections import Counter
        count = Counter(ages)
        age_keys = list(count.keys())

        res = 0

        if len(age_keys) == 1:
            return (len(ages) * (len(ages) - 1))

        for i in range(len(age_keys)):
            # print(count[i])
            if count[age_keys[i]] > 1:
                if age_keys[i] >= 15:
                    res += (count[age_keys[i]] * (count[age_keys[i]]-1))

            for j in range(i+1, len(age_keys)):
                if age_keys[i]<=0.5*age_keys[j]+7 or age_keys[i] > age_keys[j]:
                    pass
                else:
                    res = res + count[age_keys[i]] * count[age_keys[j]]

                if age_keys[j]<=0.5*age_keys[i]+7 or age_keys[j] > age_keys[i]:
                    pass
                else:
                    res = res + count[age_keys[i]] * count[age_keys[j]]
        return res

    def numFriendRequests3(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        of course, use list would be more convenient
        """
        nums = [0 for i in range(121)]  # 记录各个年龄段有多少人
        sums = [0 for i in range(121)]  # 记录小于对应年龄段的人数多少
        count = 0

        for i in range(len(ages)):
            nums[ages[i]] += 1

        for i in range(121):
            sums[i] += sums[i - 1] + nums[i]

        for i in range(15, 121):
            if nums[i] == 0:
                continue
            j = sums[i] - sums[int(i / 2) + 7]
            j = j - 1
            count += nums[i] * j
        return count


if __name__ == "__main__":
    ages = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
    s = Solution()
    print(s.numFriendRequests(ages))
    print("-----------")
    ages = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
    print(s.numFriendRequests2(ages))


