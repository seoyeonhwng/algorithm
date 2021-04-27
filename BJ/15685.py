mat = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(int(input())):
    y, x, d, g = map(int, input().split(' '))

    # x,y에서 d방향으로 g세대까지 드래곤 커브 생성
    mat[x][y] = 1
    prev = [d] # 이전 드래곤의 이동
    dirs = [d]

    for _ in range(g+1):
        for i in dirs:
            x += dx[i]
            y += dy[i]
            #x, y = x + dx[i], y + dy[i]
            mat[x][y] = 1

        # 다음 이동은 이전 드래곤 + 1 / 거꾸로
        dirs = [(p + 1) % 4 for p in prev]
        dirs.reverse()
        prev = prev + dirs
       
answer = 0
for i in range(100):
    for j in range(100):
        if mat[i][j] and mat[i+1][j] and mat[i][j+1] and mat[i+1][j+1]:
            answer += 1
print(answer)