class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        exponent = log(n, 3)
        return abs(exponent - round(exponent)) < 1e-10