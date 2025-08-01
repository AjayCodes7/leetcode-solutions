class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(1, rowIndex+2):
            curr = [0]*i
            curr[0] = 1
            curr[-1] = 1
            if i > 2:
                prev = result
                for i in range(1, i - 1):
                    curr[i] = prev[i] + prev[i-1]
            result = curr[:]
        return result