class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # get diagonal matrix 
        diagonal = collections.defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal[i-j].append(mat[i][j])
                
        # sort
        for value in diagonal.values():
            value.sort()
            
        # to matrix
        sorted_mat = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sorted_mat[i][j] = diagonal.get(i - j).pop(0)
        
        return sorted_mat

"""
이차원 배열에서 같은 대각선에 있는 원소는 i-j가 같다!
요놈을 이용하여 i-j를 key로 하는 딕셔너리를 사용하는 것이 핵심!
"""