class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        @lru_cache(None)
        def dfs(subset, O , I):
            if subset == len(strs):
                return 0

            zeros = strs[subset].count('0')
            ones = strs[subset].count('1')

            exclude = dfs(subset+1, O, I)
            include = 0
            if O + zeros <= m and I + ones <= n:
                include = 1 + dfs(subset+1, O + zeros, I + ones)

            return max(include, exclude)
        
        return dfs(0,0,0)