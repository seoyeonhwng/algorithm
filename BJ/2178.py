def valid_pos(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or mat[x][y] == 0:
        return False
    return True

def bfs(i, j):
    # 두 노드 사이의 최단 경로를 찾는 경우 BFS를 사용한다.
    queue, path, depth = [(i, j)], [(i, j)], 0

    while queue:
        depth += 1
        # 가능한 상하좌우 좌표 넣어줌
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if x == N - 1 and y == M - 1:
                return depth

            for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if ((new_x, new_y) not in path) and valid_pos(new_x, new_y):
                    queue.append((new_x, new_y))
                    path.append((new_x, new_y))
    return depth

N, M = map(int, input().split(' '))
mat = []

for _ in range(N):
    mat.append(list(map(int, input())))

print(bfs(0, 0))