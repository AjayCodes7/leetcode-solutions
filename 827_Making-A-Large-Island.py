class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r,c):
            return (
                r < 0 or c < 0 or r == N or c == N
            )
        

        def dfs(r,c, label):
            if out_of_bounds(r,c) or grid[r][c] != 1 :
                return 0
            grid[r][c] = label
            return (1 + dfs(r+1,c, label) + dfs(r-1,c, label) + dfs(r,c+1,label) + dfs(r,c-1,label))

        size = defaultdict(list)
        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    size[label] = dfs(r,c,label)
                    label += 1
        

        def connect(r,c):
            nei = [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]
            labels = set()
            area = 1
            for nr, nc in nei:
                if out_of_bounds(nr,nc) or grid[nr][nc] == 0:
                    continue
                labels.add(grid[nr][nc])
            for i in labels:
                area += size[i]
            return area
        if not size:
            return 1
        result = max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    result = max(result, connect(r,c))
        
        return result