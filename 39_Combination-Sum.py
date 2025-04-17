class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        def backtrack(n, candidate, currSum):
            if target == currSum:
                result.append(candidate[:])
                return
            for i in range(n, len(candidates)):
                if currSum + candidates[i] <= target:
                    candidate.append(candidates[i])
                    backtrack(i,candidate,currSum+candidates[i])
                    candidate.pop()
        backtrack(0,[],0)
        return result
