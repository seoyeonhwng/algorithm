from collections import defaultdict
import sys
input = sys.stdin.readline

def df():
    for i in range(N):
        for j in range(2 * M + W):
            cur, nn, cost = edges[j]
            if dist[nn] > dist[cur] + cost:
                dist[nn] = dist[cur] + cost
                if i == N-1:
                    return True
    return False
    
for _ in range(int(input())):
    N, M, W = map(int, input().split(' '))
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split(' '))
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(W):
        a, b, c = map(int, input().split(' '))
        edges.append((a, b, -c))

    # 출발점에서 도착점까지 도착 -> 사이클 있음 + 시간 감소 -> 음의 사이클이 있니???
    dist = [sys.maxsize] * (N+1)
    result = df()
    print('YES') if result else print('NO')

   