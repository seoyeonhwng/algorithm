class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # row별 max
        # column별 max
        # original_grid - min(row_max, column_max)
        
        row_max = []
        for row in grid:
            row_max.append(max(row))
            
        column_max = []
        rotated = list(zip(*grid[::-1]))
        for col in rotated:
            column_max.append(max(col))
        
        count = 0
        for i in range(len(grid)):
            candi = row_max[i]
            for j in range(len(grid[0])):
                count += min(candi, column_max[j]) - grid[i][j]
        
        return count

"""
column별 max값 구할때 rotate 할 필요없음!

col_maxes = [max(col) for col in zip(*grid)]
"""