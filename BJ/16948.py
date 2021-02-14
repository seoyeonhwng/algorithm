from collections import deque

def bfs():
    queue = deque([(r1, c1, 0)])
    visited = set([(r1, c1)])
    
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (r2, c2):
            return count
        
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in visited:
                continue

            queue.append((nx, ny, count+1))
            visited.add((nx, ny))
    return -1



N = int(input())
r1, c1, r2, c2 = map(int, input().split(' '))

# N*N 체스판에서 (r1, c1)부터 (r2, c2)까지의 최단 거리 -> bfs!!
print(bfs())
