class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print(bin(n))
        bin_n = bin(n)
        bin_list = [each for each in bin_n]

        bin_list.pop(0)
        bin_list.pop(0)
        print(bin_list)

        res = ['0']*32
        print(res)
        res[-len(bin_list):] = bin_list[:]
        print(res)
        res.reverse()


        #
        # print(bin_list)

        res = ''.join(res)
        res_num = int(res,2)
        return res_num


s = Solution()
print(s.reverseBits(43261596))