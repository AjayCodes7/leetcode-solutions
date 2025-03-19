class Solution:
    def minOperations(self, nums: List[int]) -> int:
        start = 0
        end = 2
        n = 0
        while end <= len(nums) - 1:
            if nums[start] != 1:
                nums[start] ^= 1
                nums[start+1] ^= 1
                nums[start+2] ^= 1
                n += 1
            start += 1
            end += 1
        if nums[-1] != 0 and nums[-2] != 0:
            return n
        return -1