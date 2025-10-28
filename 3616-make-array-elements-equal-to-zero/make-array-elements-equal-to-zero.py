class Solution:

    def isValid(self, position):
        count = 0
        # left
        arr = self.nums[:]
        i = position
        direct = -1
        while -1 < i < len(self.nums):
            if arr[i] > 0:
                arr[i] -= 1
                direct = -direct
            i += direct
        if arr.count(0) == self.N:
            count += 1
        # right
        arr = self.nums[:]
        i = position
        direct = 1
        while -1 < i < len(self.nums):
            if arr[i] > 0:
                arr[i] -= 1
                direct = -direct
            i += direct
        if arr.count(0) == self.N:
            count += 1
        
        return count



    def countValidSelections(self, nums: List[int]) -> int:
        self.nums = nums
        self.N = len(nums)
        result = 0
        for i in range(self.N):
            if nums[i] == 0:
                result += self.isValid(i)
        return result