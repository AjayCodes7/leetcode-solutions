class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0]*(n) for i in range(n)]
        for query in queries:
            row1, col1, row2, col2 = query
            for row in range(row1, row2+1):
                result[row][col1] += 1
                if col2 + 1 < n:
                    result[row][col2+1] -= 1
        
        for i in range(n):
            for j in range(1, n):
                result[i][j] += result[i][j-1]
        return result