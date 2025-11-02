class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0 
        for r in range(len(nums)):
            k += nums[r]
            if k < nums[r]*(r - l + 1):
                k -= nums[l]
                l += 1
        return r - l + 1