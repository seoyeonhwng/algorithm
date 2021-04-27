def dfs(x, y, c, sx, sy, count):
    global answer
    if answer:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or mat[nx][ny] != c:
            continue
        
        # 원래는 방문하지 않은 노드만 dfs 호출
        # 방문한 노드 중에 시작점이 있다면 사이클이 있다는 뜻이므로 확인해줌
        # 시작 노드에서 최대한 깊숙히 들어가서 탐색하므로 백트리킹 해줘야함
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, c, sx, sy, count + 1)
            visited[nx][ny] = False
        elif count >= 4 and (nx, ny) == (sx, sy): # 이미 방문한 노드라면 시작점인지 체크
            answer = True
            return

N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = False
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, mat[i][j], i, j, 1)
            if answer:
                print('Yes')
                exit(0)
print('No')