class Solution:
    count = 0
    def threeSumMulti(self, A, target: int) -> int:
        if not A:
            return 0
        self.count = 0

        def DFS(A, start, target_left, c):
            print(start, target_left, c)
            if c > 3:
                return

            if target_left < 0:
                return

            if target_left == 0:
                if c == 3:
                    self.count += 1


            if start >= len(A):
                return
            else:
                for i in range(start, len(A)):
                    DFS(A, i + 1, target_left - A[i], c + 1)
                    
        DFS(A, 0, target, 0)
        return self.count



    def threeSumMulti2(self, A, target: int) -> int:
        if not A:
            return 0

        from collections import Counter
        counter = Counter(A)
        visited = set()
        res = 0
        for i in counter.keys():
            for j in counter.keys():
                k = target - j - i
                if k in counter:
                    tp = tuple(sorted([i, j, k]))

                    if tp not in visited:
                        visited.add(tp)

                        if i == j == k:
                            if counter[i] >= 3:
                                res += counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6
                        elif k == j:
                            res += counter[i] * (counter[j] - 1) * counter[j] // 2
                        elif i == j:
                            res += counter[i] * (counter[i] - 1) * counter[k] // 2
                        elif i == k:
                            res += counter[i] * (counter[i] - 1) * counter[j] // 2
                        else:
                            res += counter[i] * counter[j] * counter[k]

        return res % (10**9 + 7)

    def threeSumMulti3(self, A, target):
        # 0 <= A[i] <= 100
        count = [0] * 101
        for item in A:
            count[item] += 1

        i = 0
        res = 0
        mo = 10 ** 9 + 7
        while i <= target // 3:
            j = i
            k = target - i - j
            while j <= k:
                if k <= 100 and count[i] != 0 and count[j] != 0 and count[k] != 0:
                    if i == j == k:
                        res = (res + count[i] * (count[j] - 1) * (count[k] - 2) // 6) % mo
                    elif i == j:
                        res = (res + count[i] * (count[j] - 1) * count[k] // 2) % mo
                    elif j == k:
                        res = (res + count[i] * (count[j] - 1) * count[k] // 2) % mo
                    else:
                        res = (res + count[i] * count[j] * count[k]) % mo
                j += 1
                k = target - i - j
            i += 1
        return res


A = [0,0,0]
target = 0
s = Solution()
print(s.threeSumMulti2(A, target))