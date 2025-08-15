class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        num = log(n,4)
        if num == int(num):
            return True
        return False