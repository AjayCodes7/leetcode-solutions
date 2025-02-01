class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_fishes = 0
        visited = set()

        def is_valid(r,c):
            if(r < 0 or c < 0 or r > rows-1 or c > cols-1 or grid[r][c]==0 or (r,c) in visited):
                return False
            return True
        

        def dfs(r,c):
            if is_valid(r,c):
                visited.add((r,c))
                return (grid[r][c] + dfs(r,c+1) + dfs(r,c-1) + dfs(r+1,c) + dfs(r-1,c))
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r,c) in visited:
                    continue
                max_fishes = max(max_fishes, dfs(r,c))
        return max_fishes
                