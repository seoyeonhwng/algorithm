from collections import defaultdict

def dfs1(node):
    valid[node] = False
    for w in graph[node]:
        if valid[w]:
            dfs1(w)

def leaf_check(node):
    if not valid[node]:
        return False
    for w in graph[node]:
        if valid[w]:
            return False
    return True

def dfs2(node):
    global answer
    if leaf_check(node):
        answer += 1
        return

    for w in graph[node]:
        if valid[w]:
            dfs2(w)


N = int(input())
parent = list(map(int, input().split(' ')))
r = int(input())

graph = defaultdict(list)
for k, v in enumerate(parent):
    if v == -1:
        root = k + 1
        continue
    graph[v+1].append(k+1)

valid = [True] * (N+1)
dfs1(r+1)

answer = 0
dfs2(root)
print(answer)