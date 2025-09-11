class Solution:
    @staticmethod
    def binSearch(nums : List[int], target : int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = Solution.binSearch(nums, target)
        if idx == -1:
            return [-1, -1]
        
        start = idx
        end = idx
        while start-1 >= 0 and nums[start-1] == target:
            start -= 1
        while end+1 <= len(nums)-1 and nums[end+1] == target:
            end += 1
        return [start,end]