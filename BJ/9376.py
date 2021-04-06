from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(sx, sy, 0)])
    visited = [[-1] * (M+2) for _ in range(N+2)]
    visited[sx][sy] = 0

    while queue:
        x, y, count = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N+2 or ny < 0 or ny >= M+2:
                continue
            if visited[nx][ny] != -1 or mat[nx][ny] == '*':
                continue

            if mat[nx][ny] == '.' or mat[nx][ny] == '$':
                visited[nx][ny] = count
                queue.appendleft((nx, ny, count))
            elif mat[nx][ny] == '#':
                visited[nx][ny] = count + 1
                queue.append((nx, ny, count + 1))
    return visited

for _ in range(int(input())):
    N, M = map(int, input().rstrip().split(' '))
    tmp = [['.'] + list(input().rstrip()) + ['.'] for _ in range(N)]
    mat = [['.'] * (M+2)] + tmp + [['.'] * (M+2)]

    prison = []
    for i in range(N+2):
        for j in range(M+2):
            if mat[i][j] == '$':
                prison.append((i, j))

    one = bfs(prison[0][0], prison[0][1])
    two = bfs(prison[1][0], prison[1][1])
    three = bfs(0, 0)

    answer = sys.maxsize
    for i in range(N+2):
        for j in range(M+2):
            if mat[i][j] == '*':
                continue
            
            if one[i][j] != -1 and two[i][j] != -1 and three[i][j] != -1:
                candi = one[i][j] + two[i][j] + three[i][j]
                if mat[i][j] == '#':
                    candi -= 2
                answer = min(answer, candi)
    print(answer)

"""
* 세명이 각자 탐색을 하다가 어느 정점에서 만난다면 탈옥 가능
"""