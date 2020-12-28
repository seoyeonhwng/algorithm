def dfs(v, path):
    path.append(v)
    for w in range(N+1):
        if mat[v][w] == 1 and w not in path:
            dfs(w, path)
    return path
    
def bfs(v):
    path = [v]
    queue = [v]

    while queue:
        v = queue.pop(0)
        for w in range(N+1):
            if mat[v][w] == 1 and (w not in path):
                path.append(w)
                queue.append(w)
    return path

N, M, V = map(int, input().split(' '))
mat = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    mat[a][b] = 1
    mat[b][a] = 1

print(*dfs(V, []))
print(*bfs(V))