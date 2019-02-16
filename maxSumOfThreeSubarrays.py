class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lenth = len(nums)
        if lenth == 3 * k:
            return [0, k, 2 * k]

        sumlist = list(range(lenth - k + 1))

        for i in range(lenth - k + 1):
            summition = sum(nums[i:i + k])
            sumlist[i] = summition
        print(sumlist)

        left = list(range(lenth - k))
        right = list(range(lenth - k))

        maxsuml = sumlist[0]
        maxsumr = sumlist[lenth - k]

        for i in range(lenth - k):
            if i < k:
                left[i] = 0
            else:

                if sumlist[i - k] > maxsuml:
                    left[i] = i - k
                    maxsuml = sumlist[i - k]
                else:
                    left[i] = left[i - 1]

        for i in range(lenth - k - 1, -1, -1):
            if lenth - k - 1 - i < k:
                right[i] = lenth - k
            else:
                if sumlist[i + k] >= maxsumr:
                    right[i] = i + k
                    maxsumr = sumlist[i + k]
                else:
                    right[i] = right[i + 1]
        print(left)
        print(right)

        maxsum = sumlist[0] + sumlist[k] + sumlist[2 * k]
        reslist = [0, k, 2 * k]
        for i in range(k, lenth - 2 * k + 1):
            nowsum = sumlist[left[i]] + sumlist[right[i]] + sumlist[i]
            if nowsum > maxsum:
                maxsum = nowsum
                reslist = [left[i], i, right[i]]
        return reslist


    def maxSumOfThreeSubarrays2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        accu = [0]
        for num in nums:
            accu.append(accu[-1] + num)
        print(accu)
        left_pos = [0] * n
        total = accu[k] - accu[0]

        for i in range(k, n):
            if accu[i + 1] - accu[i + 1 - k] > total:
                left_pos[i] = i + 1 - k
                total = accu[i + 1] - accu[i + 1 - k]
            else:
                left_pos[i] = left_pos[i - 1]

        print(left_pos)

        right_pos = [n - k] * n
        total = accu[n] - accu[n - k]
        for i in reversed(range(n - k)):
            if accu[i + k] - accu[i] > total:
                right_pos[i] = i
                total = accu[i + k] - accu[i]
            else:
                right_pos[i] = right_pos[i + 1]

        print(right_pos)

        result, max_sum = [], 0
        for i in range(k, n - 2 * k + 1):
            left, right = left_pos[i - 1], right_pos[i + k]
            total = (accu[i + k] - accu[i]) + (accu[left + k] - accu[left]) + (accu[right + k] - accu[right])
            if total > max_sum:
                max_sum = total
                result = [left, i, right]
        return result


nums = [1,2,1,2,6,7,5,1]
k = 2
s = Solution()
print(s.maxSumOfThreeSubarrays(nums, k))
print(s.maxSumOfThreeSubarrays2(nums, k))