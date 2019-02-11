class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance (p, q):
            res = (p[0]- q[0])**2+(p[1]-q[1])**2
            return res

        length = []
        length.append(distance(p1, p2))
        length.append(distance(p1, p3))
        length.append(distance(p1, p4))
        length.append(distance(p2, p3))
        length.append(distance(p2, p4))
        length.append(distance(p3, p4))
        length.sort()
        if len(set(length)) != 2:
            return False

        if length[0] == length[1]:
            if length[0] == length[2]:
                if length[0] == length[3]:
                    if length[4] == length[5]:
                        if length[0] + length[0]==length[4]:
                            return True
        return False



p1=[1134,-2539]
p2=[492,-1255]
p3=[-792,-1897]
p4=[-150,-3181]


s = Solution()
print(s.validSquare(p1, p2, p3, p4))