import sys
sys.setrecursionlimit(100000)

from copy import deepcopy

def dfs(i, j, k):
    if i < 0 or i >= int(N) or j < 0 or j >= int(N):
        return
    
    if visit[i][j] or area[i][j] <= k:
        return
    
    visit[i][j] = True
    dfs(i+1, j, k)
    dfs(i-1, j, k)
    dfs(i, j+1, k)
    dfs(i, j-1, k)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for k in range(max(map(max, area))):
    # 매 높이마다 visit을 초기화하여 방문을 검사!
    visit, count = [[False] * N for _ in range(N)], 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > k and not visit[i][j]:
                dfs(i, j, k)
                count += 1

    ans = max(ans, count)

print(ans)