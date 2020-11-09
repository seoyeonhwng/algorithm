class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        def incre_row(matrix, row):
            for i in range(m):
                matrix[row][i] += 1
            return matrix
        
        def incre_col(matrix, col):
            for i in range(n):
                matrix[i][col] += 1
            return matrix
        
        matrix = [[0] * m for _ in range(n)]
        
        for row, col in indices:
            matrix = incre_row(matrix, row)
            matrix = incre_col(matrix, col)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    count += 1
        return count