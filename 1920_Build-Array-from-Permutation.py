class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda a:nums[a], nums))