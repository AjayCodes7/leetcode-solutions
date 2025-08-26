class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        maxDiag = 0
        for dim in dimensions:
            tempDiag = dim[0]*dim[0]+dim[1]*dim[1]
            tempArea = dim[0]*dim[1]
            if tempDiag >= maxDiag:
                if tempDiag > maxDiag:
                    ans = tempArea
                else:
                    ans = max(ans, tempArea)
                maxDiag = tempDiag
        return ans