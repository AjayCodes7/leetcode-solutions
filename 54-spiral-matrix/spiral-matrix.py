class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while matrix:
            # top
            result += matrix.pop(0)

            # Right
            if matrix and matrix[0]:
                for i in range(len(matrix)):
                    if matrix and matrix[i]:
                        result.append(matrix[i].pop())
            # bottom
            if matrix:
                result += matrix.pop()[::-1]

            # left
            if matrix and matrix[0]:
                for i in range(len(matrix)-1,-1,-1):
                    if matrix and matrix[i]:
                        result.append(matrix[i].pop(0))
        return result
