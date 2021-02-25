from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * (M+2) for _ in range(N+2)]
    visited[0][0] = True

    ans = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= (N+2) or ny < 0 or ny >= (M+2):
                continue
            
            if mat[nx][ny] == '*' or visited[nx][ny]:
                continue

            if mat[nx][ny] == '.':
                queue.append((nx, ny))
                visited[nx][ny] = True

            if 'A' <= mat[nx][ny] <= 'Z' and mat[nx][ny].lower() in keys: # 문 열면 '.'표시!
                mat[nx][ny] = '.'
                queue.append((nx, ny))
                visited[nx][ny] = True
            if 'a' <= mat[nx][ny] <= 'z': # 열쇠 찾을때마다 방문 리셋
                keys.add(mat[nx][ny])
                mat[nx][ny] = '.'
                queue = deque([(nx, ny)])
                visited = [[False] * (M+2) for _ in range(N+2)]
                visited[nx][ny] = True
            if mat[nx][ny] == '$':
                mat[nx][ny] = '.'
                queue.append((nx, ny))
                visited[nx][ny] = True
                ans += 1

    return ans


def get_new_mat():
    new_mat = [['.'] * (M+2)]
    for row in mat:
        tmp = ['.' if r.lower() in keys else r for r in row]
        new_mat.append(['.'] + tmp + ['.'])
    new_mat.append(['.'] * (M+2))
    return new_mat

for _ in range(int(input())):
    N, M = map(int, input().split(' '))
    mat = [list(input()) for _ in range(N)]
    keys = input()
    keys = set() if keys == '0' else set(keys)

    # mat 가장자리에 .으로 채우고 문은 없앰
    mat = get_new_mat()
    print(bfs())
