
def dfs(i, j, count):
    if i < 0 or i >= M or j < 0 or j >= N:
        return
    if label[i][j] != 0:
        return
    
    label[i][j] = count
    for d in graph[(i, j)]:
        ni, nj = i + dx[d], j + dy[d]
        dfs(ni, nj, count)


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(M)]

graph = {}
for i in range(M):
    for j in range(N):
        graph[(i, j)] = [k for k, v in enumerate(bin(mat[i][j])[2:].zfill(4)) if v == '0']

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

label, count = [[0] * N for _ in range(M)], 1
for i in range(M):
    for j in range(N):
        if label[i][j] == 0:
            dfs(i, j, count)
            count += 1
print(count-1)

# 각 label의 방의 개수를 저장
room = [0] * (count - 1)
for i in range(M):
    for j in range(N):
        room[label[i][j]-1] += 1
print(max(room))

# 벽을 하나씩 없애면서 max를 찾는다
max_room = 0
for i in range(M):
    for j in range(N):
        for d in range(4):
            if d in graph[(i, j)]:
                continue
            ni, nj = i + dx[d], j + dy[d] # 벽
            if ni < 0 or ni >= M or nj < 0 or nj >= N:
                continue

            if label[i][j] != label[ni][nj]: # 벽을 부셔서 다른 땅이랑 합친 경우
                max_room = max(max_room, room[label[i][j]-1] + room[label[ni][nj]-1])
print(max_room)
