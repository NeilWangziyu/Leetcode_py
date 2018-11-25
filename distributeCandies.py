class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        category_set = set(candies)
        print(len(category_set))
        total_cat = len(category_set)
        total_num = len(candies)
        each_num = total_num // 2
        if each_num > total_cat:
            return total_cat
        else:
            each_num


s = Solution()
candies = [1,1,2,3]
print(s.distributeCandies(candies))