from collections import defaultdict, deque
from copy import deepcopy

def spring():
    # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
    # 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
    # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
    # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
    for i in range(N):
        for j in range(N):
            len_t = len(tree[i][j])
            for k in range(len_t):
                if tree[i][j][k] <= energy[i][j]:
                    energy[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 해당 나이의 나무는 죽어서 양분이됨
                    for _ in range(k, len_t):
                        energy[i][j] += tree[i][j].pop() // 2
                    break

def add_tree(x, y):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        tree[nx][ny].appendleft(1)

def fall():
    # 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
    # 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
    # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
    for i in range(N):
        for j in range(N):
            for age in tree[i][j]:
                if age % 5 == 0:
                    add_tree(i, j)
            
            energy[i][j] += more[i][j]



N, M, K = map(int, input().split(' '))
more = [list(map(int, input().split(' '))) for _ in range(N)]

energy = [[5] * N for _ in range(N)] # 처음 양분 5씩 들어있음
tree = [[deque() for _ in range(N)] for _ in range(N)] # deque로 선언!!
for _ in range(M):
    x, y, z = map(int, input().split(' '))
    tree[x-1][y-1].append(z)

for _ in range(K):
    spring()
    fall()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)

