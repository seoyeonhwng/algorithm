class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def valid_pos(r, c, n):
            return r + n <= M and c + n <= N
        
        def all_ones(r, c, n):
            for i in range(r, r+n):
                for j in range(c, c+n):
                    if matrix[i][j] == 0:
                        return False
            return True
        
        # dp[i] : 크기가 i이고 모든 값이 1인 사각형들의 좌상단 좌표를 기록
        dp = collections.defaultdict(list)
        M, N = len(matrix), len(matrix[0])
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1:
                    dp[1].append((i, j))
        
        for i in range(2, min(M, N)+1):
            for r, c in dp[i-1]:
                if not valid_pos(r, c, i):
                    continue
                if not all_ones(r, c, i):
                    continue
                dp[i].append((r, c))
        
        return sum([len(v) for v in dp.values()])

    """
    [빠른 풀이]
    - 점화식 : dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    - [[1,1],[1,1]] 에서 (1,1)을 제외한 나머지 세개의 값이 모두 1이어야 (1,1)의 값이 2가 된다!!!!

    class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix
        M, N = len(matrix), len(matrix[0])
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return sum(chain(*dp))
    """