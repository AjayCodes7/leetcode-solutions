class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # result = []
        # idx = 0
        # for i in nums:
        #     if i == pivot:
        #         result.insert(idx,i)
        #     elif i > pivot:
        #         result.append(i)
        #     else:
        #         result.insert(idx,i)
        #         idx += 1
        # return result

        i1, j1 = 0, len(nums) - 1
        i2, j2 = 0, j1
        res = [0] * (j1+1)
        while i1 < len(nums):
            if nums[i1] < pivot:
                res[i2] = nums[i1]
                i2 += 1
            if nums[j1] > pivot:
                res[j2] = nums[j1]
                j2 -= 1
            i1, j1 = i1 + 1 , j1 - 1
        for i in range(i2, j2+1):
            res[i] = pivot
        return res