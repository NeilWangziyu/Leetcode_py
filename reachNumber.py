class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        其实我没有懂这题什么意思
        ？？
        """
        if target == 0:
            return 0

        if target < 0:
            target = abs(target)

        total_length =0
        i = 0
        while(total_length < target):
            i += 1
            total_length += i

        # 若走到第i步正好到达target位置，则需要i - 1(因为在for循环时多加了1)
        # 若走到第i步时，多了奇数个数，则需要两步
        # 若走到第i步时，多了偶数个数，则需要一步
        if total_length == target:
            return i

        else:

            delta = total_length - target
            if delta % 2 == 0:
                return i
            else:
                if i % 2 == 0:
                    return i+1
                else:
                    return i + 2



    def xx(self,num):
        import math
        print((math.sqrt(8.00*abs(num)+1)-1)/2)
        print(math.ceil((math.sqrt(8.00*abs(num)+1)-1)/2))


s = Solution()
print(s.reachNumber(4))
print(s.xx(4))