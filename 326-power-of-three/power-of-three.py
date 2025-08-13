class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        exponent = log(n, 3)
        print(exponent)
        # return abs(exponent - round(exponent)) < 1e-10
        return 3**int(exponent) == n or 3**int(exponent + 1e-10) == n