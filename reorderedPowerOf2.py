class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # run out of time
        def check(num):
            if num == 0:
                return True
            while(num % 2 == 0):
                num = num / 2
            if num == 1:
                return True
            else:
                return False

        def all_subnums(num_list):
            res = []
            if not num_list:
                return []
            if len(num_list) == 1:
                return [num_list]
            for i, num in enumerate(num_list):
                n = num_list[:i]+num_list[i+1:]
                for each in all_subnums(n):
                    res.append([num] + each)
            return res


        if N in [0,1,2,4,8,16,32]:
            return True
        num_list = list(str(N))
        # print(num_list)
        if len(num_list) == 1:
            res = [num_list]
        else:
            res = all_subnums(num_list)
        # print(res)
        for eachsub in res:
            if eachsub[0] != '0':
                num = int("".join(eachsub))
                if check(num):
                    return True
        return False

    def reorderedPowerOf2_1(self, N):
        """
        执行用时 : 32 ms, 在Reordered Power of 2的Python提交中击败了100.00% 的用户
        内存消耗 : 11.8 MB, 在Reordered Power of 2的Python提交中击败了27.78% 的用户
        Use Hash, and check every 2**i to see if any of the number matches
        """
        if N == 1:
            return True
        num = str(N)
        hash = {str(i): 0 for i in range(10)}
        for n in num:
            hash[n] = hash[n] + 1

        ans = 1
        for i in range(32):
            ans = ans * 2
            str_ans = str(ans)
            if len(str_ans) > len(num) + 1:
                return False
            if len(str_ans) == len(num):
                from copy import copy
                old_hash = copy(hash)
                for s in str_ans:
                    hash[s] -= 1
                flag = True
                for j in range(10):
                    if hash[str(j)] != 0:
                        hash = old_hash
                        flag = False
                        break
                if flag:
                    return True
        return False


s = Solution()
# print(s.reorderedPowerOf2(N=3))
# print(s.reorderedPowerOf2(N=10))
# print(s.reorderedPowerOf2(N=46))
print(s.reorderedPowerOf2(N=76276711))
print(s.reorderedPowerOf2_1(N=76276711))