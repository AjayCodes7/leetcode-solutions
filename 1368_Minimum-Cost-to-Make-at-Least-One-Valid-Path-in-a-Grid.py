class Solution:
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def is_valid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minCost = [[float("inf")]*cols for i in range(rows)]
        minCost[0][0] = 0

        deque = collections.deque([(0,0)])

        while deque:
            row, col = deque.popleft()

            for _dir, (x,y) in enumerate(self.dirs):
                new_row, new_col = row + x, col + y
                cost = 0 if grid[row][col] == _dir + 1 else 1

                if(
                    self.is_valid(new_row, new_col, rows, cols) and minCost[row][col] + cost < minCost[new_row][new_col]
                ):
                    minCost[new_row][new_col] = minCost[row][col] + cost

                    if cost == 1:
                        deque.append((new_row, new_col))
                    else:
                        deque.appendleft((new_row, new_col))
        return minCost[rows-1][cols-1]