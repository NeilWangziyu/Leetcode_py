class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        a = float('inf')
        b = float('inf')
        for each in nums:
            if each <= a:
                a = each
            elif each <= b:
                b = each
            else:
                return True
        return False
