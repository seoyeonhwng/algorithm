import sys
from collections import deque

def is_valid(a, b, c):
    if a < 0 or a >= H or b < 0 or b >= M or c < 0 or c >= N:
        return False
    if box[a][b][c] != 0:
        return False
    return True

def bfs(queue):
    while queue:
        a, b, c = queue.popleft()
        candi = [(a+1,b,c), (a-1,b,c), (a,b+1,c), (a,b-1,c), (a,b,c+1), (a,b,c-1)]

        for new_a, new_b, new_c in candi:
            if is_valid(new_a, new_b, new_c):
                box[new_a][new_b][new_c] = box[a][b][c] + 1
                queue.append((new_a, new_b, new_c))


N, M, H = map(int, input().split(' '))
box = []
for _ in range(H):
    tmp = []
    for _ in range(M):
        tmp.append(list(map(int, input().split(' '))))
    box.append(tmp)

# i, j, k로 box접근
# bfs의 depth -> 맨처음 익어있는 토마토를 큐에 다 넣는다! 그다음 BFS
queue = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

bfs(queue)

# box에 0이 있으면 불가능!
# 최소 시간은 box의 값들 중 max
answer = 1
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 0:
                print(-1)
                sys.exit()
            answer = max(answer, box[i][j][k])
print(answer-1)

