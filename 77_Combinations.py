class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(i,combination):
            if len(combination) == k:
                result.append(combination[:])
                return
            if i > n:
                return
            # Include
            combination.append(i)
            backtrack(i+1,combination)
            # Exclude
            combination.pop()
            backtrack(i+1,combination)
        backtrack(1,[])
        return result