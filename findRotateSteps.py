class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        flag = 0
        total_step = 0
        # flag stand for index of ring
        ring_list = list(ring)
        print(ring_list)
        for each in key:
            count = 0
            while(ring_list[flag]!=each):
                if flag!=len(ring)-1:
                    count += 1
                    flag += 1
                else:
                    flag = 0
                    count += 1
            total_step += count
            total_step += 1
        return total_step





ring = "godding"
key = "gd"
s = Solution()
print(s.findRotateSteps(ring, key))
