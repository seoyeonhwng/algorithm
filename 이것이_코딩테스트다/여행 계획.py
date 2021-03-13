def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
plan = list(map(int, input().split(' ')))

# 여행계획에 헤당하는 모든 노드가 같은 집합에 속하는지 파악 -> union-find
parent = [i for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if mat[i][j] == 1:
            union_parent(i, j)

ans, val = 'YES', parent[plan[0]-1]
for i in range(1, M):
    if val != parent[plan[i]]:
        ans = 'NO'
print(ans)