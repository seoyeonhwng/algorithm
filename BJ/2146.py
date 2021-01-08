from collections import deque, defaultdict
import sys
sys.setrecursionlimit(100000)

# dfs로 돌면서 해당 값을 label로 바꿔줌
def labeling(i, j, label):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if mat[i][j] != 1:
        return

    mat[i][j] = label
    labeling(i+1, j, label)
    labeling(i-1, j, label)
    labeling(i, j+1, label)
    labeling(i, j-1, label)

def bfs(v):
    global ans
    queue = deque()
    dist = [[-1] * N for _ in range(N)]

    # v로 라벨링된 섬을 찾는다
    for i in range(N):
        for j in range(N):
            if mat[i][j] == v:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        a, b = queue.popleft()

        for new_a, new_b in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
            if new_a < 0 or new_a >= N or new_b < 0 or new_b >= N:
                continue
            
            # 새로운 섬에 닿은 경우 -> 값을 갱신
            if mat[new_a][new_b] != v and mat[new_a][new_b] != 0:
                ans = min(ans, dist[a][b])
                return
            
            if mat[new_a][new_b] == 0 and dist[new_a][new_b] == -1:
                queue.append((new_a, new_b))
                dist[new_a][new_b] = dist[a][b] + 1


N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# 각각 섬들을 2부터 숫자로 라벨링!!
label = 2
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            labeling(i, j, label)
            label += 1
          
# 각 섬별로 bfs하면서 다른 섬까지의 최소 거리를 찾는다!!
ans = sys.maxsize
for l in range(2, label+1):
    bfs(l)
print(ans)