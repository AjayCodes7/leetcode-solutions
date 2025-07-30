class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        streak = maxval = res = 0
        for num in nums:
            if num > maxval:
                maxval = num
                streak = 0
                res = 0
            
            if num == maxval:
                streak += 1
            else:
                streak = 0
            
            res = max(res,streak)
        return res