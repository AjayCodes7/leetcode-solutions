class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xSteps = abs(x-z)
        ySteps = abs(y-z)
        if xSteps == ySteps:
            return 0
        elif xSteps < ySteps:
            return 1
        else:
            return 2