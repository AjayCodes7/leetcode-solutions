class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)

    def dfs(self, nums: List[float]) -> bool:
        # if not nums:
        #     return False
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 1e-6
        # Try all pairs of numbers with all operations
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Perform all operations on the pair (num_list[i], num_list[j])
                for operation in range(6):
                    next_list = self.get_next_list(nums, i, j, operation)
                    # If successful combination is found, return True
                    if next_list and self.dfs(next_list):
                        return True
        # If no combination resulted in 24, return False
        return False
    
    def get_next_list(self, num_list: List[float], first_index: int, second_index: int, operation: int) -> List[float]:
        """ Method to create a new list by applying an operation to a pair of numbers. """
        next_list = [num_list[k] for k in range(len(num_list)) if k != first_index and k != second_index]
      
        # Perform the operation based on the operation index
        if operation == 0: # Addition
            next_list.append(num_list[first_index] + num_list[second_index])
        elif operation == 1: # Subtraction (first - second)
            next_list.append(num_list[first_index] - num_list[second_index])
        elif operation == 2: # Subtraction (second - first)
            next_list.append(num_list[second_index] - num_list[first_index])
        elif operation == 3: # Multiplication
            next_list.append(num_list[first_index] * num_list[second_index])
        elif operation == 4: # Division (first / second), check for division by zero
            if num_list[second_index] != 0:
                next_list.append(num_list[first_index] / num_list[second_index])
            else:
                return []
        elif operation == 5: # Division (second / first), check for division by zero
            if num_list[first_index] != 0:
                next_list.append(num_list[second_index] / num_list[first_index])
            else:
                return []
        return next_list
