from collections import deque

def dfs(x, y, t, visited, recur):
    visited[x][y] = True
    recur.append((x, y))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or mat[nx][ny] != t:
            continue

        if (not visited[nx][ny]) and dfs(nx, ny, t, visited, recur) and len(recur) >= 4:
            return True
        if (nx, ny) in recur and len(recur) >= 4:
            return True

        recur.remove((x, y))
        return False

        
N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 'No'
for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        recur = []
        is_cycle = dfs(i, j, mat[i][j], visited, recur)
        print(i, j, is_cycle)
#         if is_cycle(i, j, mat[i][j]):
#             ans = 'Yes'
#             break
# print(ans)
