class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xSteps = abs(z-x)
        ySteps = abs(z-y)
        if xSteps == ySteps:
            return 0
        if xSteps < ySteps:
            return 1
        else:
            return 2