class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(i,combination, currSum):
            #Base Case 
            if currSum == n and len(combination) == k:
                result.append(combination[:])
                return
            if i > 9 or currSum >= n or len(combination) == k:
                return
            # Include
            combination.append(i)
            backtrack(i+1,combination, currSum + i)
            # Exclude
            combination.pop()
            backtrack(i+1,combination, currSum)
        backtrack(1,[],0)
        return result