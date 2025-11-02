class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        flag = False
        l = 0 
        r = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while l < len(nums) and cur_sum + k < nums[r]*(r - l + 1):
                cur_sum -= nums[l]
                l += 1
            if cur_sum + k >= nums[r]*(r - l + 1):
                result = max(result, r-l+1)
        return result