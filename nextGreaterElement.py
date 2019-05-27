class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for each in nums1:
            found = False
            add = False
            for i in range(len(nums2)):
                if not found:
                    if nums2[i] == each:
                        found = True
                else:
                    if nums2[i] > each:
                        res.append(nums2[i])
                        add = True
                        break

            if not add:
                res.append(-1)
        return res

    def nextGreaterElement2(self, nums1, nums2):
        stack = []
        size = 0
        next_dir = {}
        for i in nums2:
            while (stack):
                if i > stack[size - 1]:
                    next_dir[stack.pop()] = i
                    size -= 1
                else:
                    break
            stack.append(i)
            size += 1
        result = [next_dir[x] if next_dir.get(x) else -1 for x in nums1]
        return result

    def nextGreaterElement3(self, nums1, nums2):
        stack = []
        dic = {}
        for i in nums2:
            while stack and stack[-1]<i:
                a=stack.pop()
                dic[a]=i
            stack.append(i)
        print(dic)
        res = []
        for j in nums1:
            if j in dic:
                res.append(dic[j])
            else:
                res.append(-1)
        return res



nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement3(nums1, nums2))
