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

# 최소 신장 트리!
N, M = map(int, input().split(' '))
edges, total = [], 0
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    edges.append((c, a, b))
    total += c

edges.sort()
result = 0
parent = [i for i in range(N)]

for edge in edges:
    c, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c

print(total - result)