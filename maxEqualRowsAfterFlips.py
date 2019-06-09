class Solution:
    def maxEqualRowsAfterFlips1(self, matrix) -> int:
        # 超时
        if not matrix:
            return 0


        res = 1
        res_old = 1

        for i in range(len(matrix)):
            tem = 0

            for j in range(i+1, len(matrix)):
                xor_res = []

                for index in range(len(matrix[0])):
                    xor_res.append(matrix[i][index]^matrix[j][index])

                if len(set(xor_res))==1:
                    tem += 1

            res = max(res, res_old+tem)

        return res

    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        s1 = set()
        for i in range(len(matrix)):
            s1.add(i)
        alll = [s1]
        for j in range(1, len(matrix[0])):
            flip = set()
            remain = set()
            for i in range(len(matrix)):
                if matrix[i][j] != matrix[i][0]:
                    flip.add(i)
                else:
                    remain.add(i)
            now = []
            for a in alll:
                s = a.intersection(remain)
                if len(s) > 1:
                    now.append(s)
                s = a.intersection(flip)
                if len(s) > 1:
                    now.append(s)
            alll = now
        ans = 1
        for a in alll:
            ans = max(ans, len(a))
        return ans



    # def maxEqualRowsAfterFlips(self, matrix) -> int:
    #     if not matrix:
    #         return 0
    #     if len(matrix) == 1:
    #         return 1
    #
    #     new_matrix = [int("".join(map(str, each)),2) for each in matrix]
    #     res = 1
    #     res_old = 1
    #     count_hash = {}
    #     for i in range(len(new_matrix)):
    #
    #         if new_matrix[i] not in count_hash:
    #             count_hash[new_matrix[i]] = 1
    #         else:
    #             count_hash[new_matrix[i]] += 1
    #     # print(count_hash)
    #     count_hash_keys = list(count_hash.keys())
    #     for i in range(len(count_hash_keys)):
    #         for j in range(i+1, len(count_hash_keys)):
    #             # print(count_hash_keys[i] ^ count_hash_keys[j])
    #             xor_num = count_hash_keys[i] ^ count_hash_keys[j]
    #             if set(bin(xor_num)[2:]) == 1 and xor_num!= 1:
    #                 res = max(res, res_old + count_hash[count_hash_keys[i]]*count_hash[count_hash_keys[j]])
    #
    #     return res



s = Solution()
matrix = [[0,1],[1,1]]
print(s.maxEqualRowsAfterFlips(matrix))
print(s.maxEqualRowsAfterFlips1(matrix))
matrix = [[0,1],[1,0]]
print(s.maxEqualRowsAfterFlips(matrix))
print(s.maxEqualRowsAfterFlips1(matrix))
matrix = [[0,0,0],[0,0,1],[1,1,0]]
print(s.maxEqualRowsAfterFlips1(matrix))
print(s.maxEqualRowsAfterFlips(matrix))
matrix = [[0,0,0],[0,0,1],[1,1,0],[1,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
print(s.maxEqualRowsAfterFlips(matrix))
print(s.maxEqualRowsAfterFlips1(matrix))

