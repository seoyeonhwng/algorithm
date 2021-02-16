from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        count, x = queue.popleft()
        if x == N-1:
            return count

        for i in range(1, mat[x]+1):
            nx = x + i
            if (0 <= nx < N) and (nx not in visited):
                queue.append((count + 1, nx))
                visited.add(nx)
    return -1



N = int(input())
mat = list(map(int, input().split(' ')))

# 0부터 N-1까지 최단거리 -> bfs!!
# 1부터 mat[i]까지 더한 값을 이동 가능
print(bfs())