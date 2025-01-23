class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid) * [0]
        cols = len(grid[0]) * [0]
        for r in range(len(rows)):
            for c in range(len(cols)):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        for r in range(len(rows)):
            for c in range(len(cols)):
                if grid[r][c] == 1:
                    if rows[r] >= 2 or cols[c] >= 2:
                        result += 1
        return result
