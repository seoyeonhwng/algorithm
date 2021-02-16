from collections import deque

def bfs():
    queue = deque([(0, S)])
    visited = set([S])

    while queue:
        count, x = queue.popleft()
        if x == D:
            return count    

        for i in [F, -B]:
            nx = x + i
            if (1 <= nx <= N) and (nx not in visited) and (nx not in police):
                queue.append((count + 1, nx))
                visited.add(nx)
    return -1


# S에서 D까지 최단 거리 -> bfs!!!
# 1부터 N까지 일렬로 나열 + +F, -B로 이동 가능, 이떄 경찰서는 방문 못함

N, S, D, F, B, K = map(int, input().split(' '))
police = set(map(int, input().split(' '))) if K > 0 else []

ans = bfs()
print('BUG FOUND') if ans == -1 else print(ans)
