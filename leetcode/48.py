class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = list(zip(*matrix[::-1]))
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]

"""
빠른 풀이
- shallow copy를 이용한다!

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
"""