class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            curr = [0]*i
            curr[0] = 1
            curr[-1] = 1
            if i > 2:
                prev = result[-1]
                for i in range(1, i - 1):
                    curr[i] = prev[i] + prev[i-1]
            result.append(curr[:])
        return result
                
