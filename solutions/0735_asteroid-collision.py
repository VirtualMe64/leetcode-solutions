# Problem: https://leetcode.com/problems/asteroid-collision
# Runtime: 69 ms

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        out = [asteroids[0]]
        for astr in asteroids[1:]:
            destroy = False
            if astr < 0:
                while len(out) > 0:
                    top = out.pop()
                    if top < 0:
                        out.append(top)
                        out.append(astr)
                        break

                    diff = top + astr
                    if diff > 0:
                        out.append(top)
                        break
                    elif diff == 0:
                        destroy = True
                        break
                if len(out) == 0 and not destroy:
                    out.append(astr)
            else:
                out.append(astr)

        return out