class Solution:
    max_length = 0
    count = 0
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        超时了可惜
        理应用动态规划的方法求解
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        res = []
        def bfs(depth, start, res_list):
            res.append(res_list)
            if len(res_list) > self.max_length:
                self.max_length = len(res_list)
                self.count = 1
            elif len(res_list) == self.max_length:
                self.count += 1

            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    if res_list == [] or nums[i]> res_list[-1]:
                        bfs(depth+1, i+1, res_list+[nums[i]])
                    # else:
                    #     if nums[i]> res_list[-1]:
                    #         bfs(depth + 1, i + 1, res_list + [nums[i]])
        bfs(0, 0, [])

        return self.count


    def findNumberOfLIS2(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            利用动态规划
        """








nums = [1,3,5,4,7]
# nums = [3,1,2]
# nums = [1,2,4,3]
# nums= [2,2,2,2,2]
# nums = [0,7,1,3,6,0,0,4,9,10]
# nums = [0,7,1,3,6,0,0,4,9,10,5,7,2,10,3,3,0,5,7,2,3,5,8,-9,10,6,7,1,1,2,9,0,1,5,10,8,1,9,6,7,5,8,4,-1,6,5,7,0,3,4,8,9,9,3,7,9,1,3,10,7,9,5,10,1,2,9,9,7,3,5,2,0,3,1,8,7,9,2,6,4,1,6,5]
s = Solution()
print(s.findNumberOfLIS(nums))
# print(s.findNumberOfLIS3(nums))