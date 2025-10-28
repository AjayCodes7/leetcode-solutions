class Solution:

    # def isValid(self, position):
    #     count = 0
    #     # left
    
    #     arr = self.nums[:]
    #     i = position
    #     direct = -1
    #     while -1 < i < len(self.nums):
    #         if arr[i] > 0:
    #             arr[i] -= 1
    #             direct = -direct
    #         i += direct
    #     if arr.count(0) == self.N:
    #         count += 1
    #     # right
    #     arr = self.nums[:]
    #     i = position
    #     direct = 1
    #     while -1 < i < len(self.nums):
    #         if arr[i] > 0:
    #             arr[i] -= 1
    #             direct = -direct
    #         i += direct
    #     if arr.count(0) == self.N:
    #         count += 1
        
    #     return count



    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        count = 0
        for num in nums:
            if num == 0:
                right_sum = total - left_sum

                if right_sum == left_sum:
                    count += 2
                elif abs(right_sum - left_sum) == 1:
                    count += 1
            left_sum += num
        return count