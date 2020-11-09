class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(mat)):
            count += mat[i][i]
        
        for i in range(len(mat)-1, -1, -1):
            count += mat[i][len(mat)-1-i]
        
        if len(mat) % 2 == 1:
            count -= mat[len(mat)//2][len(mat)//2]
        return count