class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids:
            return []

        keep = True
        while(keep):
            keep = False
            new_star = []
            i = 0
            while(i<len(asteroids)-1):
                print(i)
                if (asteroids[i] * asteroids[i+1]>0) or (asteroids[i]<0 and asteroids[i+1]>0):
                    new_star.append(asteroids[i])
                    i += 1

                else:
                    keep = True
                    if abs(asteroids[i]) > abs(asteroids[i+1]):
                        new_star.append(asteroids[i])
                    elif abs(asteroids[i]) < abs(asteroids[i+1]):
                        new_star.append(asteroids[i+1])
                    else:
                        pass
                    i += 2
                if i == len(asteroids) - 1:
                    new_star.append(asteroids[i])
            asteroids = new_star
            print(asteroids)
            if len(asteroids) == 1:
                return asteroids
        return asteroids


    def asteroidCollision2(self, asteroids):
#         利用stark来进行判断！
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                if not stack:
                    stack.append(a)
                else:
                    while (stack):
                        if stack[-1] > abs(a):
                            break
                        elif stack[-1] == abs(a):
                            stack.pop()
                            break
                        elif stack[-1] < 0:
                            stack.append(a)
                            break
                        else:
                            stack.pop()
                            if not stack:
                                stack.append(a)
                                break
        return stack



s = Solution()
print(s.asteroidCollision2([-2,1,-2,-2]))
