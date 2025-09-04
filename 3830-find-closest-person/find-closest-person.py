class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xsteps = abs(z-x)
        ysteps = abs(z-y)
        if xsteps == ysteps:
            return 0
        if xsteps < ysteps:
            return 1
        else:
            return 2