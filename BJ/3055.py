from collections import deque, defaultdict

def bfs(queue):
    count = defaultdict(list)

    while queue:
        v, a, b = queue.popleft()

        for new_a, new_b in [(a+1,b), (a-1,b), (a, b+1), (a, b-1)]:
            if new_a < 0 or new_a >= R or new_b < 0 or new_b >= C:
                continue
            
            # 물인 경우는 상하좌우 중에 비어있는 곳이 있다면 물로 채워줌
            if v == '*' and mat[new_a][new_b] == '.':
                queue.append(('*', new_a, new_b))
                mat[new_a][new_b] = '*'
            # 이제부터는 첫방문이고 .이거나 D인 경우만 갈 수 있다
            else:
                if visited[new_a][new_b]:
                    continue

                if mat[new_a][new_b] == '.':
                    queue.append(('.', new_a, new_b))
                    visited[new_a][new_b] = True
                    count[(new_a, new_b)] = count[(a, b)] + 1
                elif mat[new_a][new_b] == 'D':
                    return count[(a, b)] + 1
        return 'KAKTUS'



R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

# S와 D사이의 최단 거리 -> BFS
# 물과 고슴도치 둘다 이동하므로 둘다 큐에 넣는다!
queue = deque()

# 물 먼저 넣는다.
for i in range(R):
    for j in range(C):
        if mat[i][j] == '*':
            queue.append(('*', i, j))

# S 넣는다.
for i in range(R):
    for j in range(C):
        if mat[i][j] == 'S':
            queue.append(('S', i, j))
            visited[i][j] = True

print(bfs(queue))