class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        maxSofar = nums[0]
        minSofar = nums[0]

        for curr in nums[1:]:
            if curr < 0:
                maxSofar, minSofar = minSofar, maxSofar
            
            maxSofar = max(maxSofar*curr,curr)
            minSofar = min(minSofar*curr,curr)

            maxProd = max(maxSofar, maxProd)
        return maxProd
