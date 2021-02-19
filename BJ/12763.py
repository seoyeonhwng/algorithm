from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, 0, 1)]
    dp = [[sys.maxsize] * (T+1) for _ in range(N+1)]
    dp[1][0] = 0

    while heap:
        time, cost, node = heapq.heappop(heap)
        if dp[node][time] != cost:
            continue

        for w, wt, wc in graph[node]:
            if time + wt > T or cost + wc > M:
                continue
            if dp[w][time + wt] > cost + wc:
                dp[w][time + wt] = cost + wc
                heapq.heappush(heap, (time + wt, cost + wc, w))
    return dp


N = int(input())
T, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(int(input())):
    a, b, t, c = map(int, input().split(' '))
    graph[a].append((b, t, c))
    graph[b].append((a, t, c))

# 1번 노드부터 N번 노드까지 최소 비용
dp = dijkstra()
ans = min(dp[N])
print(-1) if ans == sys.maxsize else print(ans)