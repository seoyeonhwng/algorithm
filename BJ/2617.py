from collections import defaultdict
import sys

# 각 노드에 도달할 수 있는 최소 거리 -> 플로이드 와샬!
N, M = map(int, input().split(' '))
matrix = [[sys.maxsize] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split(' '))
    matrix[a-1][b-1] = 1

for i in range(N):
    matrix[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

ans = 0
for row in matrix:
    outdegree = sum([1 for r in row if r != sys.maxsize and r != 0])
    if outdegree > N // 2:
        ans += 1

for col in zip(*matrix):
    indegree = sum([1 for c in col if c != sys.maxsize and c != 0])
    if indegree > N // 2:
        ans += 1
print(ans)