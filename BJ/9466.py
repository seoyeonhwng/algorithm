from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def dfs(n):
    global teams
    if visited[n]:
        return
    
    visited[n] = True
    path.append(n)

    w = graph[n]
    if visited[w] and w in path:
        teams += path[path.index(w):] # w부터 사이클 시작이므로 잘라줌
        return

    dfs(w)

# 사이클이 있는 경우 팀 -> DFS
for _ in range(int(input())):
    N = int(input())
    graph = {}

    for i, v in enumerate(list(map(int, input().split(' ')))):
        graph[i+1] = v

    teams = []
    visited = [False] * (N+1) # 사이클 아니였던 애들도 재탐색 안함

    for n in range(1, N+1):
        if visited[n]:
            continue

        path = []
        dfs(n)

    print(N - len(teams))