class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        result = []
        direction = 1
        x = y = 0
        while(True):
            result.append(mat[x][y])
            if x == n-1 and y == m-1:
                return result
            if direction:
                if x == 0 and y != m-1:
                    direction = 0
                    y += 1
                elif y == m-1:
                    direction = 0
                    x += 1
                else:
                    x -= 1
                    y += 1
            else:
                if y == 0 and x != n-1:
                    direction = 1
                    x+=1
                elif x == n-1:
                    direction = 1
                    y += 1
                else:
                    x += 1
                    y -= 1
            