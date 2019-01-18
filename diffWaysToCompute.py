class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        i_list = []
        for index in range(len(input)):
            if not input[index].isdigit():
                i_list.append(index)

        res = []
        # print(i_list)

        for i in i_list:
            # print(input[:i], input[i+1:])
            left = self.diffWaysToCompute(input[:i])
            right = self.diffWaysToCompute(input[i+1:])
            # print(left, right)
            if input[i] == '+':
                for each_l in left:
                    for each_r in right:
                        res.append(each_l+each_r)
            elif input[i] == '-':
                for each_l in left:
                    for each_r in right:
                        res.append(each_l-each_r)
            elif input[i] == '*':
                for each_l in left:
                    for each_r in right:
                        res.append(each_l*each_r)
        return res

    def diffWaysToCompute2(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.res1 = []
        self.res2 = []
        self.ans = []
        self.mysplit(input)
        if len(self.res1) == 0:
            return [self.res2[0]]
        self.dfs(self.res2, self.res1, [])
        return self.ans

    def dfs(self, nums, signs, res):
        if not signs:
            self.ans.append(res[0])
            return
        if len(nums) > 0:
            self.dfs(nums[1:], signs, res + [nums[0]])
        l1 = len(nums)
        if len(signs) > l1:
            pos = signs[-l1 - 1]
            newsigns = signs[:]
            newsigns.pop(-l1 - 1)
            if pos == '+':
                res[-2] += res[-1]
                self.dfs(nums, newsigns, res[:-1])
            elif pos == '-':
                res[-2] -= res[-1]
                self.dfs(nums, newsigns, res[:-1])
            else:
                res[-2] *= res[-1]
                self.dfs(nums, newsigns, res[:-1])

    def mysplit(self, s):
        temp = ''
        nums = []
        for i in s:
            if i in ['+', '-', '*']:
                self.res1.append(i)
                nums.append(int(temp))
                temp = ''
            else:
                temp += i
        nums.append(int(temp))
        self.res2 = nums[:]


input = "2*3-4*5"
s = Solution()
print(s.diffWaysToCompute(input))
print(s.diffWaysToCompute2(input))