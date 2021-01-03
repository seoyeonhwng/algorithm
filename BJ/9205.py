from collections import deque

# 상근이네 집과 페스티벌 장소까지의 최단 거리를 구함 -> BFS!
def bfs(start):
    queue = deque([(start[0], start[1], 1000)])
    path = set([start])

    while queue:
        x, y, beer = queue.popleft()
        if (x, y) == end:
            return True

        for a, b in nodes:
            if (beer >= abs(x-a) + abs(y-b)) and ((a, b) not in path):
                path.add((a, b))
                queue.append((a, b, 1000))
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    nodes = []
    start = tuple(map(int, input().split(' ')))
    for _ in range(N):
        nodes.append(tuple(map(int, input().split(' '))))
    end = tuple(map(int, input().split(' ')))
    nodes.append(end)

    if bfs(start):
        print('happy')
    else:
        print('sad')