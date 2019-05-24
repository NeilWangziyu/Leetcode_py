class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lights = [False for _ in range(n)]
        for i in range(1, n+1):
            init = i-1
            while(init < n):
                lights[init] = not lights[init]
                init += i

            # print(lights)
        return lights.count(True)

    def bulbSwitch(self, n):
        import math
        return int(math.sqrt(n))

    # 首先思考：灯泡i会被按几次？这其实相当于求i有几个因子
    # 比如灯泡8, 一共会被按4次，分别是第一轮
    # 第二轮
    # 第四轮
    # 第八轮
    #
    # 一开始灯都是灭的，所以如果i有k个因子，且k为奇数，那么最终灯就亮，如果为偶数，灯就灭。 那么问题就转化成了，求1..n每个数分别有几个因子。 最直观的做法就是，枚举i，然后计算i的因子数。怎么计算呢？ 最直观的做法就是枚举j = 0..i，count += i % j == 0 ? 1: 0;
    # 这里有个优化的点，假如x * y = z，显然z % y == 0
    # 且z % x == 0。 也就是说你只要需要枚举j从到1..根号i，count += i % j == 0? 2: 0;
    #
    # 在写完上面的式子之后你突然可以发现，在根号i的左边每发现一个j使得i % j == 0，那么根号i的右边一定存在一个k同样满足i % k == 0，一次枚举会把count + 2。而我们关心的其实是最终count为奇数还是偶数！！通过枚举，count最终的结果都是偶数，当且仅当
    # i可以被开根号时，count才会是奇数！
    #
    # 然后其实问题转换成了，求数字1..n中有几个数能开更开得尽（结果是整数）
    #
    # 想到这里，你就可以一个O(n)
    # 的枚举来完成了吗？ 其实还可以优化！
    #
    # 想想，在1..n中，假设n等于100，1 * 1
    # 2 * 2
    # 3 * 3
    # 4 * 4...
    # 10 * 10
    # 的结果都小于等于100，换句话说，1 * 1...根号n * 根号n
    # 都 <= n，所以求1..n里有几个开根号能开尽的数，其实就是求根号n向下取整等于几。


n = 1000000
s = Solution()
print(s.bulbSwitch(n))