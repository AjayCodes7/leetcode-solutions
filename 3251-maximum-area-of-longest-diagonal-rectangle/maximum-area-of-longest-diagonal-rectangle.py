class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        maxDiag = 0
        for l,w in dimensions:
            tempDiag = l*l+w*w
            tempArea = l*w
            if (tempDiag, tempArea) > (maxDiag, ans):
                ans = tempArea
                maxDiag = tempDiag
        return ans
