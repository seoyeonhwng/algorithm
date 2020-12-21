
def dfs(i, j, path):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    
    if area[i][j] == '#' or area[i][j] == 0:
        return

    area[i][j] = '#'
    path.append((i, j))
    dfs(i+1, j, path)
    dfs(i-1, j, path)
    dfs(i, j+1, path)
    dfs(i, j-1, path)


N = int(input())
area = [list(map(int, list(input()))) for _ in range(N)]

count = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            path = []
            dfs(i, j, path)
            count.append(len(path))

print(len(count))
for c in sorted(count):
    print(c)