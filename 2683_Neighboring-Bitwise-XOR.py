class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Approach: 1
        # result = 0
        # for i in derived:
        #     result ^= i
        # return result== 0
        
        # Approach: 2
        return sum(derived) % 2 == 0