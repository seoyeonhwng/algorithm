from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(sx, sy, ex, ey):
    queue = deque([(sx, sy, 0)])
    visited = [[False] * C for _ in range(R)]

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (ex, ey):
            return count
        
        if visited[x][y]:
            continue

        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            
            if i == mat[x][y]:
                queue.appendleft((nx, ny, count))
            else:
                queue.append((nx, ny, count+1))


# rs, cs 부터 rd, cd까지의 최단거리 
# 현재 방향과 같은 방향이면 0, 아니면 1씩 증가 -> 다익스트라!!

R, C = map(int, input().split(' '))
mat = [list(map(int, list(input().rstrip()))) for _ in range(R)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(int(input())):
    rs, cs, rd, cd = map(int, input().rstrip().split(' '))
    print(bfs(rs-1, cs-1, rd-1, cd-1))

"""
가중치가 0, 1 + 다익스트라 + 시간 초과 일때 할 수 있는 것들
* heappop, heappush 대신 appendleft, append로
* sys.stdin.readline으로 인풋받기
* visited는 이차원 배열로
"""