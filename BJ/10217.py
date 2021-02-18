from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def run():
    # dp[node][cost] = 최소 time을 저장 -> cost는 M이 최대니까
    dp = [[sys.maxsize] * (M+1) for _ in range(N+1)]
    dp[1][0] = 0

    for m in range(M+1):
        for node in range(1, N+1):
            if dp[node][m] == sys.maxsize:
                continue

            dist = dp[node][m]
            for w, wc, wd in graph[node]:
                if m + wc > M:
                    continue
                dp[w][m + wc] = min(dp[w][m + wc], dist + wd)
    return dp
    
    
for _ in range(int(input())):
    N, M, K = map(int, input().split(' '))
    graph = defaultdict(list)
    for _ in range(K):
        u, v, c, d = map(int, input().split(' '))
        graph[u].append((v, c, d))

    dp = run()
    ans = min(dp[N])
    print('Poor KCM') if ans == sys.maxsize else print(ans)
