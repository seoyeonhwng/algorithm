from collections import deque

def bfs(s_x, s_y):
    mat = [[False] * N for _ in range(N)]
    mat[s_x][s_y] = True
    queue = deque([(s_x, s_y, 0)])

    while queue:
        x, y, count = queue.popleft()
        if x == e_x and y == e_y:
            return count

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or mat[nx][ny]:
                continue
            
            mat[nx][ny] = True
            queue.append((nx, ny, count + 1))


dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for _ in range(int(input())):
    N = int(input())
    s_x, s_y = map(int, input().split(' '))
    e_x, e_y = map(int, input().split(' '))

    # 나이트의 최소 이동 개수 -> BFS!
    print(bfs(s_x, s_y))