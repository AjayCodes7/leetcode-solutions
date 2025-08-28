class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        # Traverse form right -> left(x = 0) and then top -> bottom (y = 0)
        # Need to create a temporary list of every diagonal
        # get the sorted list and update the grid

        n = len(grid)

        x = 0
        for y in range(n-1, -1,-1):
            i = x
            j = y
            temp = []
            while i < n and j < n:
                temp.append(grid[i][j])
                i += 1
                j += 1
            temp.sort()
            idx = 0

            i = x
            j = y
            while i < n and j < n:
                grid[i][j] = temp[idx]
                idx += 1
                i += 1
                j += 1
            
        y = 0
        for x in range(n-1, -1,-1):
            i = x
            j = y
            temp = []
            while i < n and j < n:
                temp.append(grid[i][j])
                i += 1
                j += 1

            temp.sort(reverse = True)
            idx = 0
            i = x
            j = y
            while i < n and j < n:
                grid[i][j] = temp[idx]
                idx += 1
                i += 1
                j += 1
            
        return grid