class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)

    def dfs(self, nums: List[float]) -> bool:
        
        if not nums:
            return False

        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 1e-6

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for operation in range(6):
                    next_list = self.get_next_list(nums, i, j, operation)
                    if next_list and self.dfs(next_list):
                        return True
        return False
    
    def get_next_list(self, num_list: List[float], first_index: int, second_index: int, operation: int) -> List[float]:
        next_list = [num_list[k] for k in range(len(num_list)) if k != first_index and k != second_index]
      
        if operation == 0:
            next_list.append(num_list[first_index] + num_list[second_index])
        elif operation == 1:
            next_list.append(num_list[first_index] - num_list[second_index])
        elif operation == 2:
            next_list.append(num_list[second_index] - num_list[first_index])
        elif operation == 3:
            next_list.append(num_list[first_index] * num_list[second_index])
        elif operation == 4:
            if num_list[second_index] != 0:
                next_list.append(num_list[first_index] / num_list[second_index])
            else:
                return []
        elif operation == 5:
            if num_list[first_index] != 0:
                next_list.append(num_list[second_index] / num_list[first_index])
            else:
                return []
        return next_list
