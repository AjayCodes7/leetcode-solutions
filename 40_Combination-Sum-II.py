class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]
        def backtrack(n, candidate, currSum):
            if target == currSum:
                if candidate not in result:
                    result.append(candidate[:])
                    return
            if n == len(candidates):
                return
            if currSum > target:
                return
            hash = set()
            for i in range(n,len(candidates)):
                if candidates[i] not in hash:
                    hash.add(candidates[i])
                    candidate.append(candidates[i])
                    backtrack(i+1,candidate,currSum+candidates[i])
                    candidate.pop()
        backtrack(0,[],0)
        return result