# Problem: https://leetcode.com/problems/walking-robot-simulation-ii
# Runtime: 44 ms

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * width + 2 * height - 4
        self.pos = 0
        self.started = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perimeter
        self.started = True

    def getPos(self) -> List[int]:
        if self.pos < self.width: # Bottom wall
            return (self.pos, 0)
        elif self.pos < self.width + self.height - 1: # Right wall
            return (self.width - 1, self.pos - self.width + 1)
        elif self.pos < 2 * self.width + self.height - 2: # Top wall
            progress = self.pos - self.width - self.height + 2
            return (self.width - progress - 1, self.height - 1)
        else: # Left wall
            progress = self.pos - self.width - self.height - self.width + 3
            return (0, self.height - 1 - progress)

    def getDir(self) -> str:
        if self.pos == 0:
            return "South" if self.started else "East"
        elif self.pos < self.width: # Bottom wall
            return "East"
        elif self.pos < self.width + self.height - 1: # Right wall
            return "North"
        elif self.pos < 2 * self.width + self.height - 2: # Top wall
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()