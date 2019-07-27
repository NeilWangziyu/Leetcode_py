
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and not quadTree2.val):
            return quadTree1
        elif (quadTree2.isLeaf and quadTree2.val) or (quadTree1.isLeaf and not quadTree1.val):
            return quadTree2
        else:
            l1 = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            l2 = self.intersect(quadTree1.topRight,quadTree2.topRight)
            l3 = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            l4 = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            if l1.isLeaf and l2.isLeaf and l3.isLeaf and l4.isLeaf and l1.val == l2.val == l3.val == l4.val:
                return l1
            return Node(None,False,l1,l2,l3,l4)

    def intersect2(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and not quadTree2.val):
            return quadTree1
        elif (quadTree1.isLeaf and not quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            return quadTree2
        else:
            tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            return Node(True, True, None, None, None,None) if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val and tr.val and bl.val and br.val else Node(
                False, False, tl, tr, bl, br)
