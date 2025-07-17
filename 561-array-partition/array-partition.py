class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # flag = True
        # result = 0
        # for i in sorted(nums):
        #     if flag:
        #         result += i
        #     flag = not flag
        # return result

        nums.sort()
        result = 0
        for i in range(0, len(nums),2):
            result += nums[i]
        return result
