import random
# random.uniform(-1,1)
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while (True):
            x = random.uniform(-1, 1) * self.radius
            y = random.uniform(-1, 1) * self.radius
            if x ** 2 + y ** 2 <= self.radius ** 2:
                return [x + self.x_center, y + self.y_center]

import math
class Solution2(object):
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x = x_center
        self.y = y_center
    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = (random.random() ** 0.5) * self.radius
        theta = random.uniform(0, 2 * math.pi)
        return [r * math.cos(theta) + self.x, r * math.sin(theta) + self.y]
