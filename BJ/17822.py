from collections import deque
import sys
sys.setrecursionlimit(100000)

def do_rotation(x, d, k):
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향
    for i in range(N):
        if (i+1) % x == 0:
            tmp = k if d == 0 else -k
            mat[i].rotate(tmp)

def dfs(i, j, val):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if visited[i][j] or mat[i][j] != val:
        return

    visited[i][j] = True
    path.append((i, j))

    dfs(i + 1, j, val)
    dfs(i - 1, j, val)
    dfs(i, (j + 1) % M, val)
    dfs(i, (j - 1) % M, val)

def remove_adj(candi):
    for x, y in candi:
        mat[x][y] = 0

def get_avg():
    total, count = 0, 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] != 0:
                total += mat[i][j]
                count += 1

    if count == 0:
        return 0
    return total / count


N, M, T = map(int, input().split(' '))
mat = []
for _ in range(N):
    mat.append(deque(list(map(int, input().split(' ')))))

for _ in range(T):
    x, d, k = map(int, input().split(' '))
    do_rotation(x, d, k)

    # dfs로 인접하고 숫자가 같은 곳을 모두 찾음
    visited = [[False] * M for _ in range(N)]
    candi = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and mat[i][j] != 0:
                path = []
                dfs(i, j, mat[i][j])
                if len(path) > 1:
                    candi += path

    if candi:
        remove_adj(candi)
    else:
        avg = get_avg()
        for i in range(N):
            for j in range(M):
                if mat[i][j] != 0 and mat[i][j] > avg:
                    mat[i][j] -= 1
                elif mat[i][j] != 0 and mat[i][j] < avg:
                    mat[i][j] += 1

answer = 0
for row in mat:
    answer += sum(row)
print(answer)