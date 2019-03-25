class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        minx = max(rec1[0], rec2[0])
        maxx = min(rec1[2], rec2[2])
        miny = max(rec1[1], rec2[1])
        maxy = min(rec1[3], rec2[3])
        if minx < maxx and miny < maxy:
            return True
        else:
            return False

    def isRectangleOverlap2(self, rec1, rec2) -> bool:
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False
        elif rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        else:
            return True


