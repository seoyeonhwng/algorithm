class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # summed area table
        summed = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summed[i][j] = mat[i][j]
                summed[i][j] += summed[i][j-1] if j > 0 else 0
                summed[i][j] += summed[i-1][j] if i > 0 else 0
                summed[i][j] -= summed[i-1][j-1] if (i > 0 and j > 0) else 0
        
        out = [[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                min_row, max_row = max(0, i-K), min(len(mat)-1, i+K)
                min_col, max_col = max(0, j-K), min(len(mat[0])-1, j+K)
                out[i][j] = summed[max_row][max_col]
                out[i][j] -= summed[max_row][min_col-1] if min_col > 0 else 0
                out[i][j] -= summed[min_row-1][max_col] if min_row > 0 else 0
                out[i][j] += summed[min_row-1][min_col-1] if (min_col > 0 and min_row > 0) else 0
        
        return out

"""
* cell(i, j) : (0, 0)부터 (i, j)까지 모든 원소의 합
-> I(x, y) = i(x, y) + I(x, y-1) + I(x-1, y) - I(x-1, y-1)
"""