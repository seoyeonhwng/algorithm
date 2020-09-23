# 다익스트라 풀이
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def valid_pos(a, b):
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                return True
            return False
        
        queue = [[grid[0][0], (0, 0)]]
        dist = collections.defaultdict(int)
        
        while queue:
            time, pos = heapq.heappop(queue)
            if pos not in dist:
                dist[pos] = time
                
                # 아래, 오른쪽 이동 가능
                i, j = pos
                if valid_pos(i+1, j):
                    alt = time + grid[i+1][j]
                    heapq.heappush(queue, [alt, (i+1, j)])
                    
                if valid_pos(i, j+1):
                    alt = time + grid[i][j+1]
                    heapq.heappush(queue, [alt, (i, j+1)])
        
        return dist[(len(grid)-1, len(grid[0])-1)]
        
# 다이나믹 프로그래밍 풀이
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def valid_pos(a, b):
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                return True
            return False
        
        dp = collections.defaultdict(int)
        dp[(0,0)] = grid[0][0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                    
                if not valid_pos(i-1, j):
                    dp[(i-1, j)] = sys.maxsize
                if not valid_pos(i, j-1):
                    dp[(i, j-1)] = sys.maxsize
                    
                dp[(i, j)] = grid[i][j] + min(dp[(i-1, j)], dp[(i, j-1)])
                
        return dp[(len(grid)-1, len(grid[0])-1)]
        