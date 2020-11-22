class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, col = len(rowSum), len(colSum)
        mat = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                value = min(rowSum[i], colSum[j])
                mat[i][j] = value
                rowSum[i] -= value
                colSum[j] -= value
        
        return mat
