class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xSteps = abs(z-x)
        ySteps = abs(z-y)
        if xSteps == ySteps:
            return 0
        return 1 if xSteps < ySteps else 2