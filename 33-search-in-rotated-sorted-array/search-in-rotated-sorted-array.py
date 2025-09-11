class Solution:
    def bin_search(self, iter, target):
        left = 0
        right = len(iter)-1
        while left <= right:
            mid = (left+right)//2
            if iter[mid] == target:
                return mid
            elif target < iter[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                idx = i + 1
                break
        first = self.bin_search(nums[:idx], target)
        last = self.bin_search(nums[idx:], target)
        if first == last:
            return -1
        if first != -1:
            return first
        return idx + last