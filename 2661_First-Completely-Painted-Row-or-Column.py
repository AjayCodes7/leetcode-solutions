class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        location = {}
        m = len(mat)
        n =  len(mat[0])

        for i in range(m):
            for j in range(n):
                location[mat[i][j]] = (i,j)

        rows = [0] * m
        cols = [0] * n

        for i in range(len(arr)):
            r,c = location[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i