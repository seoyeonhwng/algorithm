from itertools import combinations
from collections import deque
from copy import deepcopy
import sys

# 0의 위치를 찾아서 3개의 조합을 구한다
# 각 조합에 대해 dfs()한다
# 0의 개수를 최대로 갱신

def bfs(maps, queue, visited):
    # 신규방문에 0인 곳으로만 이동 가능
    while queue:
        a, b = queue.popleft()

        for new_a, new_b in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
            if new_a < 0 or new_a >= N or new_b < 0 or new_b >= M:
                continue
            if not visited[new_a][new_b] and maps[new_a][new_b] == 0:
                queue.append((new_a, new_b))
                visited[new_a][new_b] = True
                maps[new_a][new_b] = 2


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

zero, virus = [], deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            zero.append((i, j))
        elif mat[i][j] == 2:
            virus.append((i, j))
            visited[i][j] = True

ans = -sys.maxsize
for wall in combinations(zero, 3):
    maps = deepcopy(mat)
    visit = deepcopy(visited)
    queue = deepcopy(virus)

    for a, b in wall:
        maps[a][b] = 1
    bfs(maps, queue, visit)
    
    count = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                count += 1
    ans = max(ans, count)
print(ans)