from collections import defaultdict
import sys

def df(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur, nn, cost = edges[j]
            if dist[cur] != sys.maxsize and dist[nn] > dist[cur] + cost:
                dist[nn] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

N, M = map(int, input().split(' '))
edges = []
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    edges.append((a, b, c))

# 1번 노드부터 나머지 노드까지의 최단 거리 + 음수 가중치 -> 벨만포드!!!
dist = [sys.maxsize] * (N+1)
result = df(1)

if result:
    print(-1)
else:
    for i in range(2, N+1):
        print(-1) if dist[i] == sys.maxsize else print(dist[i])