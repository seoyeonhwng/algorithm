from collections import defaultdict
import heapq
import sys

# 1번부터 K까지 최단거리 + K부터 X까지 최단 거리 -> 플로이드 와샬!
# 노드의 개수가 100개면 플로이드 와샬로 풀 수 있음
N, M = map(int, input().split(' '))

matrix = [[sys.maxsize] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split(' '))
    matrix[a][b] = 1
    matrix[b][a] = 1
X, K = map(int, input().split(' '))

for i in range(1, N+1):
    matrix[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

if matrix[1][K] == sys.maxsize or matrix[K][X] == sys.maxsize:
    print(-1)
else:
    print(matrix[1][K] + matrix[K][X])
