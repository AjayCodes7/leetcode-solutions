class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        result = []
        cursum = 0
        for i in range(1,n):
            result.append(i)
            cursum += i
        result.append(-cursum)
        return result
        