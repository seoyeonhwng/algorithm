from collections import defaultdict

def dfs1(node):
    win.add(node)

    for w in graph[node]:
        if w not in win:
            dfs1(w)

def dfs2(node):
    lose.add(node)

    for w in graph_r[node]:
        if w not in lose:
            dfs2(w)


N, M = map(int, input().split(' '))
graph = defaultdict(list)
graph_r = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph_r[b].append(a)

ans = 0
for node in range(1, N+1):
    win, lose = set(), set()
    dfs1(node)
    dfs2(node)
    if len(win) + len(lose) == N+1:
        ans += 1

print(ans)