class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jumpUpto = 0
        index = 0
        while index <= jumpUpto:
            jumpUpto = max(jumpUpto, index + nums[index])
            if jumpUpto >= len(nums) - 1:
                return True
            index += 1
        return False
