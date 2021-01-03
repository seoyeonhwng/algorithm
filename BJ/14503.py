
# dfs!!!
def clean(x, y, d):
    global ans
    # 현재 위치를 청소한다.
    if maps[x][y] == 0:
        maps[x][y] = 2 # 재방문 방지
        ans += 1
    
    for _ in range(4):
        nd = (d + 3) % 4 # 왼쪽 방향 회전
        nx = x + dx[nd]
        ny = y + dy[nd]
        if maps[nx][ny] == 0:
            clean(nx, ny, nd) # 1번부터 진행
            return
        
        # 왼쪽 방향에 청소할 공간이 없다면, 회전
        d = nd
    
    # 네 방향 모두 청소가 되어있거나 벽인 경우
    nd = (d + 2) % 4 # 뒤로 이동
    nx = x + dx[nd]
    ny = y + dy[nd]
    if maps[nx][ny] == 1:
        return
    
    clean(nx, ny, d)


N, M = map(int, input().split(' '))
r_x, r_y, r_d = map(int, input().split(' '))

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split(' '))))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
clean(r_x, r_y, r_d)
print(ans)