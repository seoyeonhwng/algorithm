N, M = map(int, input().split(' '))
x, y, d = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
visited = set([(x, y)])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turn = 0

while True:
    nd = (d + 3) % 4 # 반시계 방향 90도 회전
    nx, ny = x + dx[nd], y + dy[nd] # 왼쪽 방향

    if (nx, ny) not in visited and mat[nx][ny] == 0:
        x, y, d = nx, ny, nd
        visited.add((nx, ny))
        turn = 0
    else:
        d = nd
        turn += 1

    if turn == 4:
        nd = (d + 2) % 4 # 뒤로 이동
        nx, ny = x + dx[nd], y + dy[nd]

        if mat[nx][ny] == 1:
            print(len(visited))
            break
        x, y = nx, ny
        turn = 0
        
