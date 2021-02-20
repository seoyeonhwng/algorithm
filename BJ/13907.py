from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    dp = [[sys.maxsize] * (N+1) for _ in range(N+1)]
    dp[S][0] = 0

    for count in range(N):
        for n in range(1, N+1):
            if dp[n][count] == sys.maxsize:
                continue

            for w, wc in graph[n]:
                dp[w][count+1] = min(dp[w][count+1], dp[n][count] + wc)
    return dp

N, M, K = map(int, input().split(' '))
S, D = map(int, input().split(' '))

graph = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split(' '))
    graph[a].append((b, w))
    graph[b].append((a, w))
p_list = [int(input()) for _ in range(K)]

# S에서 D까지 최단 거리 합 -> 다익스트라!
dp = dijkstra()
print(min(dp[D]))

for p in p_list:
    for i in range(N+1):
        dp[D][i] += i * p
    print(min(dp[D]))

# S에서 D까지 가는 경로들의 도로 개수도 영향을 주기 때문에 같이 저장!
# dp[node][count] = cost 식으로 구할때는 dp로만 구할수도 있음!