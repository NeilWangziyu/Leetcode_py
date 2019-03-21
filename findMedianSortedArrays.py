class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        O(nlog(n))
        """
        num = nums1+nums2
        num.sort()
        # print(num)
        if len(num)%2==0:
            mid = len(num)//2-1
            return (num[mid]+num[mid+1])/2
        else:
            mid = len(num)//2
            return num[mid]


    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        O(n)
        """
        m = len(nums1)
        n = len(nums2)
        p, q = 0, 0
        if (n + m) % 2 == 0:
            mid = ((n + m) // 2 - 1, (n + m) // 2)
        else:
            mid = ((n + m) // 2, (n + m) // 2)
        all = []
        while(p < m and q < n):
            if nums1[p] <= nums2[q]:
                all.append(nums1[p])
                p += 1
            else:
                all.append(nums2[q])
                q += 1
        if p >= m:
            while q < n:
                all.append(nums2[q])
                q += 1
        else:
            while p < m :
                all.append(nums1[p])
                p += 1
        return (all[mid[0]] + all[mid[1]]) / 2


    def findMedianSortedArrays3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        O(log(n+m))
        https://blog.csdn.net/yutianzuijin/article/details/11499917
        """
        def findKth(nums1, n1, nums2, n2, K):
            # 默认nums1  <= nums2
            if n1 > n2:
                return findKth(nums2, n2, nums1, n1, K)
            if n1 == 0 :
                return nums2[K - 1]
            if K == 1:
                return min(nums1[0], nums2[0])

            pa = min(K//2, n1)
            pb = K - pa

            if (nums1[pa - 1] < nums2[pb - 1]):
                return findKth(nums1[pa:], n1-pa, nums2, n2, K-pa)
            elif (nums1[pa - 1] > nums2[pb - 1]):
                return findKth(nums1, n1, nums2[pb:], n2-pb, K-pb)

            else:
                return nums1[pa - 1]

        total = len(nums2) + len(nums1)
        if total % 2 != 0:
            return findKth(nums1, len(nums1), nums2, len(nums2), total//2+1)
        else:
            return (findKth(nums1, len(nums1), nums2, len(nums2), total//2) + findKth(nums1, len(nums1), nums2, len(nums2), total//2 + 1)) / 2






    def findMedianSortedArrays4(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        O(log(min(m, n)))
        key
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        # make sure len(A) is shorter
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0




if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(s.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 3]
    nums2 = [2]
    print(s.findMedianSortedArrays3(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(s.findMedianSortedArrays3(nums1, nums2))

