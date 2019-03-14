class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        from collections import Counter
        counter = Counter(nums)
        print(counter)
        res = 0
        for i in counter.keys():
            if i in counter and i + 1 in counter:
                if counter[i] + counter[i+1] > res:
                    res = counter[i] + counter[i+1]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findLHS(nums=[4289383,46930886,81692777,14636915,57747793,24238335,19885386,49760492,96516649,89641421]))