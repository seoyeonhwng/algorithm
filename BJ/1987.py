import sys
from collections import deque


def bfs(i, j):
    max_count = 0
    queue = set([(i, j, mat[i][j])])

    while queue:
        a, b, path = queue.pop()
        max_count = max(max_count, len(path))
        if max_count == 26:
            return 26

        for new_a, new_b in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if (0 <= new_a < R and 0 <= new_b < C) and (mat[new_a][new_b] not in list(path)):
                queue.add((new_a, new_b, path + mat[new_a][new_b]))
    return max_count


R, C = map(int, input().split(' '))
mat = []
for _ in range(R):
    mat.append(list(input()))

# 최단거리처럼 path의 count 문제 -> BFS
# BFS에서 deque를 사용하여 메모리초과가 나면 set으로 구현해보자!
print(bfs(0, 0))